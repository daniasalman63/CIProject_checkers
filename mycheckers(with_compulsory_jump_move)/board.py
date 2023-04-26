import numpy as np

from myfile import *
from pieces import Piece

class Board:
    def __init__(self, player):
        self.board = []
        self.red_left = 12
        self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()
        self.player = player
        self.jump = False
    
    def evaluate(self, player):
        """This function evaluates the score which is an 
        output from the neural network"""
        return predict_nn(self.board_to_vec(self.board), player)
    
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        """This function moves the piece from one position to another,
        it doesn't deal with removing any pieces"""
        #SWAPPING THE POSITIONS, THE POS WHERE THE PIECE WAS ACTUALLY AT WOULD BECOME 0 WHICH MEANS AN AMPTY BLOCK
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        #IF EITHER OF THE PIECE REACHES THE END OF THE BOARD WHEN A MOVE IS MADE, THE PIECE BECOMES KING
        if row == 7 or row == 0:
            piece.make_king()
            if piece.color == "white":
                self.white_kings += 1
            else:
                self.red_kings += 1
        # self.board_to_vec() 
        # print(self.vec)

    def get_piece(self, row, col):
        """This will get the piece object on the given row and column"""
        return self.board[row][col]

    def create_board(self):
        """This would create an initial board with all pieces placed at their respective positions"""
        for row in range(8):
            self.board.append([])
            for col in range (8):
                if row< 3:
                    if (row%2 == 0 and col%2 ==1) or (row%2 ==1 and col%2 == 0):
                        self.board[row].append(Piece(row, col, "white"))
                    else:
                        self.board[row].append(0)
                elif row >= 3 and row <5:
                    self.board[row].append(0)
                else:
                    if (row%2 == 0 and col%2 ==1) or (row%2 ==1 and col%2 == 0):
                        self.board[row].append(Piece(row, col, "red"))
                    else:
                        self.board[row].append(0)
        
    def board_to_vec(self, board):
        """This will convert the nested board list to a numpy array of shape (1,32)
        so that we can send the playable positions of the board to the neural 
        network in order to evaluate the score of the current position to 
        act as an heuristic of alpha-beta pruning"""
        vec = []
        for row in range(8):
            for col in range (8):
                if (row %2 == 0 and col%2 == 1) or (row%2 ==1 and col%2 == 0):
                    pos = board[row][col]
                    if pos == 0:
                        vec.append(0)
                    elif pos.color == "white":
                        if pos.king == True:
                            vec.append(3)
                        else:
                            vec.append(1)
                    else:
                        if pos.king == True:
                            vec.append(-3)
                        else:
                            vec.append(-1)
        vec = np.array(vec).reshape(1,32)
        return vec

    def remove(self, pieces):
        """This will take as input all the pieces a checker jumped over
        then those pieces would be removed from board by replacing them 
        with 0"""
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == "red":
                    self.red_left -= 1
                else:
                    self.white_left -= 1
    
    def winner(self): 
        """The winner is decided when 40 moves are made without any capture
        from either sides, the game ends then and whichever color has more pieces wins 
        otherwise if both have equal pieces then its a draw"""
        white_pieces = len(self.get_all_pieces("white"))
        red_pieces = len(self.get_all_pieces("red"))
        if white_pieces == 0:
            return "red"
        elif red_pieces == 0:
            return "white"
        elif white_pieces > red_pieces:
            return "white"
        elif red_pieces > white_pieces:
            return "red"
        else:
            return "draw"
    
    def get_valid_moves(self, piece):
        """This checks for all the valid moves a current piece has by traversing left and right diagonals"""
        moves = {}
        jump_moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == "red" or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == "white" or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, 8), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, 8), 1, piece.color, right))

        for i in moves:
            if len(moves[i]) > 0:
                jump_moves[i] = moves[i]
        if len(jump_moves)>0:
            return jump_moves, True
        else:
            return moves, False
        
    def priority_moves(self, color):
        move_lst = []
        pieces = self.get_all_pieces(color)
        for i in pieces:
            moves , jump = self.get_valid_moves(i)
            if jump == True:
                for j in moves:
                    move_lst.append(j)
        return move_lst

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        """This traverses all the left diagonals"""
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, 8)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        """This traverses all the right diagonals"""
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= 8:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, 8)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves
    