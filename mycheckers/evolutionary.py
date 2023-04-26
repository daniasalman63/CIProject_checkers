from myfile import *
import random
from game import Game
from algorithm import *
random.seed(0)

def parentSelection(chromosomes, type):
    if type == "random":
        index = np.random.choice(chromosomes, 2, replace=False) 
        
        parent1 = index[0]
        parent2 = index[1]

        if parent1 == parent2:
            print("Parents are the same??")

    elif type == "truncation":
        sorted_population = sorted(chromosomes, key=lambda chromosome: chromosome.score, reverse=True)
        parent1 = sorted_population[-1]
        parent2 = sorted_population[-2]

    elif type == "fps":
        
        total_fitness = sum(chromosome.score for chromosome in chromosomes)
        chromosome_probabilities = [chromosome.score/total_fitness for chromosome in chromosomes]
        parent1 = random.choices(chromosomes, weights=chromosome_probabilities)
        newPopulation.remove(parent1)
        parent2 = random.choices(chromosomes, weigths=chromosome_probabilities)
        

    elif type == "binary_tournament":
        parent_1 = random.choice(chromosomes)
        parent_2 = random.choice(chromosomes)

        # Choose the fittest chromosome as the first parent
        if parent_1.score > parent_2.score:
            parent1 = parent_1
        else:
            parent1 = parent_2

        # repeats for second parent
        parent_1 = random.choice(chromosomes)
        parent_2 = random.choice(chromosomes)
        if parent_1.score > parent_2.score:
            parent2 = parent_1
        else:
            parent2 = parent_2

    return parent1, parent2

         
    
def crossover(parent1, parent2):

    p1first_layer_weights, p1first_layer_bias, p1second_layer_weights, p1second_layer_bias, p1third_layer_weights,  p1third_layer_bias = parent1.getWeights()
    p2first_layer_weights, p2first_layer_bias, p2second_layer_weights, p2second_layer_bias, p2third_layer_weights,  p2third_layer_bias = parent2.getWeights()
    
    crossoverPoint1 = random.randint(0, len(p1first_layer_weights) - 1)

    o1first_layer_weights = []
    o2first_layer_weights = []

    for i in range(len(p1first_layer_weights)):
        
        o1 = np.concatenate((p1first_layer_weights[i][:crossoverPoint1],(p2first_layer_weights[i][crossoverPoint1:])))
        o2 = np.concatenate((p2first_layer_weights[i][:crossoverPoint1], p1first_layer_weights[i][crossoverPoint1:]))

        o1first_layer_weights.append(o1)
        o2first_layer_weights.append(o2)

    crossoverPoint2 = random.randint(0, len(p1first_layer_bias) - 1)
   
    o1first_layer_bias = []
    o2first_layer_bias = []

    for i in range(len(p1first_layer_bias)):

        o1 = np.concatenate((p1first_layer_bias[i][:crossoverPoint2], p2first_layer_bias[i][crossoverPoint2:]))
        o2 = np.concatenate((p2first_layer_bias[i][:crossoverPoint2], p1first_layer_bias[i][crossoverPoint2:]))

        o1first_layer_bias.append(o1)
        o2first_layer_bias.append(o2)

    crossoverPoint3 = random.randint(0, len(p1second_layer_weights) - 1)
   
    o1second_layer_weights = []
    o2second_layer_weights = []

    for i in range(len(p1second_layer_weights)):

        o1 = np.concatenate((p1second_layer_weights[i][:crossoverPoint3], p2second_layer_weights[i][crossoverPoint3:]))
        o2 = np.concatenate((p2second_layer_weights[i][:crossoverPoint3], p1second_layer_weights[i][crossoverPoint3:]))

        o1second_layer_weights.append(o1)
        o2second_layer_weights.append(o2)

    crossoverPoint4 = random.randint(0, len(p1second_layer_bias) - 1)

    o1second_layer_bias = []
    o2second_layer_bias = []

    for i in range(len(p1second_layer_bias)):

        o1 = np.concatenate((p1second_layer_bias[i][:crossoverPoint4], p2second_layer_bias[i][crossoverPoint4:]))
        o2 = np.concatenate((p2second_layer_bias[i][:crossoverPoint4], p1second_layer_bias[i][crossoverPoint4:]))

        o1second_layer_bias.append(o1)
        o2second_layer_bias.append(o2)

    crossoverPoint5 = random.randint(0, len(p1third_layer_weights) - 1)

    o1third_layer_weights = []
    o2third_layer_weights = []

    for i in range(len(p1third_layer_weights)):

        o1 = np.concatenate((p1third_layer_weights[i][:crossoverPoint5], p2third_layer_weights[i][crossoverPoint5:]))
        o2 = np.concatenate((p2third_layer_weights[i][:crossoverPoint5], p1third_layer_weights[i][crossoverPoint5:]))

        o1third_layer_weights.append(o1)
        o2third_layer_weights.append(o2)

    crossoverPoint6 = random.randint(0, len(p1third_layer_bias) - 1)

    o1third_layer_bias = []
    o2third_layer_bias = []

    for i in range(len(p1third_layer_bias)):

        o1 = np.concatenate((p1third_layer_bias[0][:crossoverPoint6], p2third_layer_bias[0][crossoverPoint6:]))
        o2 = np.concatenate((p2third_layer_bias[0][:crossoverPoint6], p1third_layer_bias[0][crossoverPoint6:]))

        o1third_layer_bias.append(o1)
        o2third_layer_bias.append(o2)

    offspring1 = []
    offspring1.append(o1first_layer_bias)
    offspring1.append(o1second_layer_bias)
    offspring1.append(o1third_layer_bias)

    offspring1.append(o1first_layer_weights)
    offspring1.append(o1second_layer_weights)
    offspring1.append(o1third_layer_weights)

    offspring2 = []
    offspring2.append(o2first_layer_bias)
    offspring2.append(o2second_layer_bias)
    offspring2.append(o2third_layer_bias)

    offspring2.append(o2first_layer_weights)
    offspring2.append(o2second_layer_weights)
    offspring2.append(o2third_layer_weights)

    return offspring1, offspring2

def mutation(offspring1, offspring2, mutationRate):

    o1first_layer_bias, o1second_layer_bias, o1third_layer_bias, o1first_layer_weights, o1second_layer_weights, o1third_layer_weights = offspring1
    o2first_layer_bias, o2second_layer_bias, o2third_layer_bias, o2first_layer_weights, o2second_layer_weights, o2third_layer_weights = offspring2
    
    if random.uniform(0, 1) < mutationRate:
        rand_nums = np.random.randint(0, len(o1first_layer_bias[0]) - 1, size=2)
        o1first_layer_bias[0][rand_nums[0]] = np.random.normal(0, 1)
        o1first_layer_bias[0][rand_nums[1]] = np.random.normal(0, 1)
        

        rand_nums = np.random.randint(0, len(o2first_layer_bias[0]) - 1, size=2)
        o2first_layer_bias[0][rand_nums[0]] = np.random.normal(0, 1)
        o2first_layer_bias[0][rand_nums[1]] = np.random.normal(0, 1)

    if random.uniform(0, 1) < mutationRate:
        rand_nums = np.random.randint(0, len(o1second_layer_bias[0]) - 1, size=2)
        o1second_layer_bias[0][rand_nums[0]] = np.random.normal(0, 1)
        o1second_layer_bias[0][rand_nums[1]] = np.random.normal(0, 1)
        
        rand_nums = np.random.randint(0, len(o2second_layer_bias[0]) - 1, size=2)
        o2second_layer_bias[0][rand_nums[0]] = np.random.normal(0, 1)
        o2second_layer_bias[0][rand_nums[1]] = np.random.normal(0, 1)

    if random.uniform(0, 1) < mutationRate:
        rand_nums = np.random.randint(0, len(o1third_layer_bias[0]) - 1, size=2)
        o1third_layer_bias[0][rand_nums[0]] = np.random.normal(0, 1)
        o1third_layer_bias[0][rand_nums[1]] = np.random.normal(0, 1)

        rand_nums = np.random.randint(0, len(o2third_layer_bias[0]) - 1, size=2)
        o2third_layer_bias[0][rand_nums[0]] = np.random.normal(0, 1)
        o2third_layer_bias[0][rand_nums[1]] = np.random.normal(0, 1)

    for i in range(len(o1first_layer_weights) - 1):
        if random.uniform(0, 1) < mutationRate:
            rand_nums = np.random.randint(0, len(o1first_layer_weights[0]) - 1, size=2)
            o1first_layer_weights[i][rand_nums[0]] = np.random.normal(0, 1)
            o1first_layer_weights[i][rand_nums[1]] = np.random.normal(0, 1)

            rand_nums = np.random.randint(0, len(o2first_layer_weights[0]) - 1, size=2)
            o2first_layer_weights[i][rand_nums[0]] = np.random.normal(0, 1)
            o2first_layer_weights[i][rand_nums[1]] = np.random.normal(0, 1)


    for i in range(len(o1second_layer_weights) - 1):
        if random.uniform(0, 1) < mutationRate:
            rand_nums = np.random.randint(0, len(o1second_layer_weights[0]) - 1, size=2)
            o1second_layer_weights[i][rand_nums[0]] = np.random.normal(0, 1)
            o1second_layer_weights[i][rand_nums[1]] = np.random.normal(0, 1)

            rand_nums = np.random.randint(0, len(o2second_layer_weights[0]) - 1, size=2)
            o2second_layer_weights[i][rand_nums[0]] = np.random.normal(0, 1)
            o2second_layer_weights[i][rand_nums[1]] = np.random.normal(0, 1)


    for i in range(len(o1third_layer_weights) - 1):
        if random.uniform(0, 1) < mutationRate:
            rand_nums = np.random.randint(0, len(o1third_layer_weights[0]) - 1, size=2)
            o1third_layer_weights[i][rand_nums[0]] = np.random.normal(0, 1)
            o1third_layer_weights[i][rand_nums[1]] = np.random.normal(0, 1)

            rand_nums = np.random.randint(0, len(o2third_layer_weights[0]) - 1, size=2)
            o2third_layer_weights[i][rand_nums[0]] = np.random.normal(0, 1)
            o2third_layer_weights[i][rand_nums[1]] = np.random.normal(0, 1)

    mutatedOffspring1 = []
    mutatedOffspring1.append(o1first_layer_bias)
    mutatedOffspring1.append(o1second_layer_bias)
    mutatedOffspring1.append(o1third_layer_bias)

    mutatedOffspring1.append(o1first_layer_weights)
    mutatedOffspring1.append(o1second_layer_weights)
    mutatedOffspring1.append(o1third_layer_weights)

    mutatedOffspring2 = []
    mutatedOffspring2.append(o2first_layer_bias)
    mutatedOffspring2.append(o2second_layer_bias)
    mutatedOffspring2.append(o2third_layer_bias)

    mutatedOffspring2.append(o2first_layer_weights)
    mutatedOffspring2.append(o2second_layer_weights)
    mutatedOffspring2.append(o2third_layer_weights)

    return mutatedOffspring1, mutatedOffspring2

def calculateFitness(population):
    
    for i in range(len(population) - 1):

        player1 = population[i]

        challengers = population[:i] +  population[i+1:]

        randomPlayers = np.random.choice(challengers, size=3, replace=False)

        for player2 in randomPlayers:
            obj = Game(player1, player2)
            counter = 0
            while counter < 40:
                # if obj.turn == "red":
                #     opponent = "white"
                # else:
                #     opponent = "red"
                old_pieces = obj.board.red_left + obj.board.white_left
                value, new_board = alpha_beta(obj.get_board(), 3, float("-inf"), float("inf"), obj.turn, obj)
                # value, new_board = minimax(obj.get_board(), 3, obj.turn, obj)
                #print(obj.turn)
                # print(new_board.board)
                obj.ai_move(new_board)
                # if obj.turn == "red":
                #     opponent = "white"
                # else:
                #     opponent = "red"
                new_pieces = obj.board.red_left + obj.board.white_left
                difference = old_pieces - new_pieces
                if difference > 0:
                    counter = 0
                else:
                    counter += 1
                # print(counter)
                # print("DIFF: ", old_pieces - new_pieces)
                winner = obj.winner()

                if winner == "red":
                    best_player = obj.player1
                else:
                    best_player = obj.player2

            if winner=="draw":
                player1.score +=1
                player2.score +=1
            else:
                best_player.score +=2

            print("game complete")
            



def survivorSelection(newPopulation, type):

    finalPopulation = []
        
    if type == "truncation":

        tup = []
        for i in newPopulation:
            tup.append((i.score, i))
        
        sortedlist = sorted(tup, key=lambda x: x[0], reverse=True)

        for pop in sortedlist:
            finalPopulation.append(pop[1])

        finalPopulation =  finalPopulation[:10]
    
    elif type == "fps":
        for i in range(10):
            total_fitness = sum(chromosome.score for chromosome in newPopulation)
            chromosome_probabilities = [chromosome.score/total_fitness for chromosome in newPopulation]
            choice = random.choices(newPopulation, weights=chromosome_probabilities)
            newPopulation.remove(choice[0])
            finalPopulation.append(random.choices(choice[0]))

    elif type == "binary_tournament":
         
        for i in range(10):
        # Choose two random parents from the population
            parent1 = random.choice(newPopulation)
            parent2 = random.choice(newPopulation)

            # Choose the fittest chromosome as the first parent
            if parent1.score > parent2.score:
                finalPopulation.append(parent1)
            else:
                finalPopulation.append(parent2)
    
    return finalPopulation

def NueroEvolution(population, generations):

    chromosomes = []

    #Initialise random population
    for i in range(population):
        chromosomes.append(evolutionary_player(i))

    calculateFitness(chromosomes)

    for i in chromosomes:
        print(i.score)

    #print(chromosomes)
    count = 10
    
    for n in range(generations):
        print("Generation: ", n)

        parent1, parent2 = parentSelection(chromosomes, "random")

        offspring1, offspring2 = crossover(parent1, parent2)  
        print("Crossover complete")

        offspring1AfterMutation, offspring2AfterMutation = mutation(offspring1, offspring2, mutationRate=0.5)

        parent1player, parent2player = createNeuralNetwork(offspring1AfterMutation, offspring2AfterMutation, count)
        print("Mutation complete")

        newPopulation = chromosomes + [parent1player, parent2player]
        

        calculateFitness(newPopulation)
        print("Fitness Calculation complete")

        chromosomes = survivorSelection(newPopulation, "truncation")
        
        print("Generation Scores")
        for i in chromosomes:
            print(i.score)

        count += 2
    
    print("Final Scores")
    for i in chromosomes:
        print(i.score)




NueroEvolution(10, 5)

'''
while obj.winner(obj.move_limit) == None:
                value, new_board = minimax(obj.get_board(), 3, obj.turn, obj)
                #print(obj.turn)
                # print(new_board.board)
                obj.ai_move(new_board)
                winner = obj.winner(obj.move_limit)
                if winner == "red":
                    best_player = obj.player1
                else:
                    best_player = obj.player2

            if winner=="draw":
                player1.score +=1
                player2.score +=1
            else:
                best_player.score +=2

            print(winner)'''
