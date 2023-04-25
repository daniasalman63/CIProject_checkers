from copy import deepcopy
import pygame
from game import Game
from myfile import *
import time
from GUI import *
def alpha_beta(position, depth, alpha, beta, max_player, game):
    if depth == 0:
        return position.evaluate(game.board.player), position
    
    if max_player:
        if game.turn == "red":
            color_m = "white"
        else:
            color_m = "red"
        best_move = None
        for move in get_all_moves(position, color_m, game):
            evaluation = alpha_beta(move, depth-1, alpha, beta, False, game)[0]
            if evaluation > alpha:
                alpha = evaluation
                best_move = move
            if alpha >= beta:
                break
        
        return alpha, best_move
    else:
        best_move = None
        for move in get_all_moves(position, game.turn, game):
            evaluation = alpha_beta(move, depth-1, alpha, beta, True, game)[0]
            if evaluation < beta:
                beta = evaluation
                best_move = move
            if beta <= alpha:
                break
        
        return beta, best_move

def minimax(position, depth, max_player, game):
    if depth == 0:
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


def run_program():

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
    start_time = time.time()
    counter = 0
    while counter < 40:
        old_pieces = obj.board.red_left + obj.board.white_left
        # old_pieces = len(obj.board.get_all_pieces(obj.turn)) + len(obj.board.get_all_pieces(opponent))
        value, new_board = alpha_beta(obj.get_board(), 3, float("-inf"), float("inf"), obj.turn, obj)
        # value, new_board = minimax(obj.get_board(), 3, obj.turn, obj)
        print(obj.turn)
        # print(new_board.board)
        obj.ai_move(new_board)
        # root = tk.Tk()
        # gui = CheckersBoard(root, new_board.board)
        # gui.update_board(new_board.board)
        # root.mainloop()
        
        new_pieces = obj.board.red_left + obj.board.white_left
        difference = old_pieces - new_pieces
        if difference > 0:
            counter = 0
        else:
            counter += 1
        # print(counter)
        print("DIFF: ", old_pieces - new_pieces)
        winner = obj.winner()

        if winner == "red":
            best_player = obj.player1
        else:
            best_player = obj.player2

    end_time = time.time()
    print("Duration: ", end_time - start_time)

    # print(new_board.board)
    for i in new_board.board:
        print(i)
    for i in new_board.board:
        for piece in i:
            if piece !=0:
                print("PIECE COLOR: ", piece.color, " IS KING?: ", piece.king)
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

run_program()
