from copy import deepcopy
import pygame
from game import Game
from myfile import *

def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner(game.move_limit) != None:
        return position.evaluate(game.board.player), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        if game.turn == "red":
            color_m = "white"
        else:
            color_m = "red"
        for move in get_all_moves(position, color_m, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, game.turn, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves



player1 = evolutionary_player(1)
player2 = evolutionary_player(2)
obj = Game(player1, player2)
# piece = obj.board.get_piece(5, 0)
# print(piece)
# obj.select(5, 0)
# print(obj.valid_moves)
# obj.select(4, 1)
# # obj.board.board_to_vec()
# print(obj.board.board)
# # print(obj.board.vec)
# print(obj.select(2, 1))
# obj.select(3, 2)
# # obj.board.board_to_vec()
# # print(obj.board.vec)
# print(obj.move_limit)
while obj.winner(obj.move_limit) == None:
    value, new_board = minimax(obj.get_board(), 3, obj.turn, obj)
    print(obj.turn)
    # print(new_board.board)
    obj.ai_move(new_board)
    winner = obj.winner(obj.move_limit)
    if winner == "red":
        best_player = obj.player1
    else:
        best_player = obj.player2

print(new_board.board)
print("WINNER COLOR:")
print(winner)
print("WINNER PLAYER NUM:")
print(best_player.number)
print("best first layer weights:")
print(best_player.first_layer_weights)
print("best first layer bias:")
print(best_player.first_layer_bias)
print("best second layer weights:")
print(best_player.second_layer_weights)
print("best second layer bias:")
print(best_player.second_layer_bias)
print("best third layer weights:")
print(best_player.third_layer_weights)
print("best third layer bias:")
print(best_player.third_layer_bias)
