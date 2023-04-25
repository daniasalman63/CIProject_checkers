import numpy as np

from myfile import *
from pieces import Piece
from board import Board

class Game:
    def __init__(self, player1, player2):
        self.selected = None
        self.turn = "white"
        self.valid_moves = {}
        self.player1 = player1
        self.player2 = player2
        self.board = Board(player1)

    def winner(self):
        """whatever the current board situation is, decide winner accoridng to that
        using winner method from board class"""
        return self.board.winner()

    def select(self, row, col):
        """This is reponsible for selecting the piece u want to move
        and then selecting the position you want to move the piece to"""
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        """This is a private method called when self.selected is True, i.e. when you have 
        selected a piece and a position to move to"""
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
        else:
            return False

        return True

    def change_turn(self):
        "changes turn so that no player can have two consecutive turns"
        self.valid_moves = {}
        if self.turn == "red":
            self.turn = "white"
            self.board.player = self.player2
        else:
            self.turn = "red"
            self.board.player = self.player1

    def get_board(self):
        """returns current board of the game"""
        return self.board
    
    def ai_move(self, board):
        """makes a move using alpha-beta pruning"""
        if board == None:
            # print("No valid moves")
            self.change_turn()
        else:
            self.board = board
            self.change_turn()


# player1 = evolutionary_player(1)
# player2 = evolutionary_player(2)
# obj = Game(player1, player2)
# # piece = obj.board.get_piece(5, 0)
# # print(piece)
# # obj.select(5, 0)
# # print(obj.valid_moves)
# # obj.select(4, 1)
# # # obj.board.board_to_vec()
# # print(obj.board.board)
# # # print(obj.board.vec)
# # print(obj.select(2, 1))
# # obj.select(3, 2)
# # # obj.board.board_to_vec()
# # # print(obj.board.vec)
# # print(obj.move_limit)
# while obj.winner() == None:
#     value, new_board = minim

