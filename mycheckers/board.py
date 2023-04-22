import numpy as np

from myfile import *
from pieces import Piece

class Board:
    def __init__(self, player):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()
        self.player = player
    
    # def draw_squares(self, win):
    #     win.fill(BLACK)
    #     for row in range(ROWS):
    #         for col in range(row % 2, COLS, 2):
    #             pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    def evaluate(self, player):
        return predict_nn(self.board_to_vec(self.board), player)
    
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == 7 or row == 0:
            piece.make_king()
            if piece.color == "white":
                self.white_kings += 1
            else:
                self.red_kings += 1
        # self.board_to_vec() 
        # print(self.vec)

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(8):
            self.board.append([])
            for col in range(8):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, "white"))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, "red"))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        
    def board_to_vec(self, board):
        vec = []
        for row in range(8):
            for col in range(8):
                if (col%2 == (row+1)%2):
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
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == "red":
                    self.red_left -= 1
                else:
                    self.white_left -= 1
    
    def winner(self, move_limit):
        # if move_limit >= 400:
        #     return "draw"
        # if self.red_left <= 0:
        #     return "white"
        # elif self.white_left <= 0:
        #     return "red"
        
        # return None 
        if move_limit >= 200:
            white_pieces = len(self.get_all_pieces("white"))
            red_pieces = len(self.get_all_pieces("red"))
            if white_pieces > red_pieces:
                return "white"
            elif red_pieces > white_pieces:
                return "red"
            else:
                return "draw"

        white_pieces = len(self.get_all_pieces("white"))
        red_pieces = len(self.get_all_pieces("red"))
        if white_pieces == 0:
            return "red"
        elif red_pieces == 0:
            return "white"

        return None
    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == "red" or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == "white" or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, 8), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, 8), 1, piece.color, right))
    
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
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
    