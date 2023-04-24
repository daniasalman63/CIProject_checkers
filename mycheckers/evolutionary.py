from myfile import *
import random

def parentSelection(chromosomes, type):
    if type == random:
        index = np.random.choice(chromosomes, 2, replace=False) 
        
        parent1 = index[0]
        parent2 = index[1]

        if parent1 == parent2:
            print("Parents are the same??")

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
    offspring1.append(o1second_layer_weights)

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
    o2first_layer_bias, o2second_layer_bias, o2third_layer_bias, o2first_layer_weights, o2second_layer_weights, o2third_layer_weights = offspring1
    
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
    mutatedOffspring1.append(o1second_layer_weights)

    mutatedOffspring2 = []
    mutatedOffspring2.append(o2first_layer_bias)
    mutatedOffspring2.append(o2second_layer_bias)
    mutatedOffspring2.append(o2third_layer_bias)

    mutatedOffspring2.append(o2first_layer_weights)
    mutatedOffspring2.append(o2second_layer_weights)
    mutatedOffspring2.append(o2third_layer_weights)

    return mutatedOffspring1, mutatedOffspring2


def NueroEvolution(population):

    chromosomes = []

    for i in range(population):
        chromosomes.append(evolutionary_player(i))

    parent1, parent2 = parentSelection(chromosomes, random)

    offspring1, offspring2 = crossover(parent1, parent2)

    offspring1AfterMutation, offspring2AfterMutation = mutation(offspring1, offspring2, mutationRate=0.5)



NueroEvolution(2)
