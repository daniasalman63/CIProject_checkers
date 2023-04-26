import numpy as np
import random

import math

# Weight and bias dimensions for the NN
first_layer_hidden_weights = (32,90) #32,90
first_layer_hidden_bias = (1,90) #90
second_layer_hidden_weights = (90,40) #90,40 
second_layer_hidden_bias = (1,40) #40
third_layer_hidden_weights = (40,10) #40,10
third_layer_hidden_bias = (1,10) #10

class Evol_Player(object):
    def __init__(self, number, first_layer_weights, first_layer_bias, second_layer_weights, second_layer_bias, third_layer_weights, third_layer_bias):
        self.number = number
        self.score = 0
        self.first_layer_weights = first_layer_weights
        self.first_layer_bias = first_layer_bias
        self.second_layer_weights = second_layer_weights
        self.second_layer_bias = second_layer_bias
        self.third_layer_weights = third_layer_weights
        self.third_layer_bias = third_layer_bias

        self.wins = 0
        self.loss = 0
        self.draw = 0

    def getWeights(self):
        return self.first_layer_weights, self.first_layer_bias,  self.second_layer_weights, + \
               self.second_layer_bias,  self.third_layer_weights,  self.third_layer_bias

# Used in the NN
def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))

def evolutionary_player(count):
    
    first_layer_weights = np.random.normal(0, scale=1.0, size=first_layer_hidden_weights)
    first_layer_bias = np.random.normal(0, scale=1.0, size=first_layer_hidden_bias)
    second_layer_weights = np.random.normal(0, scale=1.0, size=second_layer_hidden_weights)
    second_layer_bias = np.random.normal(0, scale=1.0, size=second_layer_hidden_bias)
    third_layer_weights = np.random.normal(0, scale=1.0, size=third_layer_hidden_weights)
    third_layer_bias = np.random.normal(0, scale=1.0, size=third_layer_hidden_bias)

    return Evol_Player(count, first_layer_weights, first_layer_bias, second_layer_weights, second_layer_bias, third_layer_weights, third_layer_bias)

# Use this Neural Network as the heuristic function for the minimax tree
def predict_nn(board, player):
    #board should be given as a 1x32 np array
    first_hidden_output = sigmoid( np.dot( board, player.first_layer_weights) + player.first_layer_bias )
    second_hidden_output = sigmoid( np.dot(first_hidden_output, player.second_layer_weights) + player.second_layer_bias )
    third_layer_output = sigmoid( np.dot(second_hidden_output, player.third_layer_weights) + player.third_layer_bias )

    output = np.sum(third_layer_output)
    
    return output

def createNeuralNetwork(offspring1AfterMutation, offspring2AfterMutation, count):

    first_layer_bias1, second_layer_bias1, third_layer_bias1, first_layer_weights1, second_layer_weights1, third_layer_weights1 = offspring1AfterMutation
    first_layer_bias2, second_layer_bias2, third_layer_bias2, first_layer_weights2, second_layer_weights2, third_layer_weights2 = offspring2AfterMutation

    player1 = Evol_Player(count + 1, first_layer_weights1, first_layer_bias1, second_layer_weights1, second_layer_bias1, third_layer_weights1, third_layer_bias1)
    player2 = Evol_Player(count + 2, first_layer_weights2, first_layer_bias2, second_layer_weights2, second_layer_bias2, third_layer_weights2, third_layer_bias2)

    return player1, player2


# player1 = evolutionary_player(1)
# # board = np.array([ 1,  1,  1,  1,
# #                    1,  1,  1,  1,  
# #                    1,  1,  0,  1,  
# #                    0,  0,  0,  0, 
# #                    0,  0, 0,  0, 
# #                    1,  0,  0, 0, 
# #                    -1,  0, 0, -1, 
# #                    -1, -1, -1, -1,])
# # board = board.reshape(1, 32)
# # print(board)
# # print("SHAPE: ", board.shape)

# # nn_output = predict_nn(board, player1)
# # print(nn_output)

# actual_board = [[0, 1, 0, 1, 0, 1, 0, 1],
#                 [1, 0, 1, 0, 1, 0, 1, 0],
#                 [0, 1, 0, 1, 0, 1, 0, 1],
#                 [0, 0, 0, 0, 0, 0, 0 ,0],
#                 [0, 0, 0, 0, 0, 0, 0 ,0],
#                 [-1, 0, -1, 0, -1, 0, -1, 0],
#                 [0, -1, 0, -1, 0, -1, 0, -1],
#                 [-1, 0, -1, 0, -1, 0, -1, 0]]

# new_vec_board = []
# for i in range(len(actual_board)):
#     for j in range(len(actual_board[i])):
#         if i%2 == 0:
#             if j%2 == 1:
#                 new_vec_board.append(actual_board[i][j])
#         else:
#             if j%2 == 0:
#                 new_vec_board.append(actual_board[i][j])

# new_vec_board = np.array(new_vec_board).reshape(1, 32)
# print(new_vec_board)

# nn_output = predict_nn(new_vec_board, player1)
# print(nn_output)
