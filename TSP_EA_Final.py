# sir wasi, zain and I had collaborated with eachother
# and decided on how to go about it
# but each of us have coded it individually.
# i was not able to print the graph properly

# on a side note:
# this was an interesting implementation i came accross while browsing the internet.
# the whole code has just been written in 10 lines.
# source:https://ericphanson.com/posts/2016/the-traveling-salesman-and-10-lines-of-python/
#
# 1  import random, numpy, math, copy, matplotlib.pyplot as plt
# 2  cities = [random.sample(range(100), 2) for x in range(15)];
# 3  tour = random.sample(range(15),15);
# 4  for temperature in numpy.logspace(0,5,num=100000)[::-1]:
#5  	[i,j] = sorted(random.sample(range(15),2));
# 6 	newTour =  tour[:i] + tour[j:j+1] +  tour[i+1:j] + tour[i:i+1] + tour[j+1:];
# 7 	if math.exp( ( sum([ math.sqrt(sum([(cities[tour[(k+1) % 15]][d] - cities[tour[k % 15]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]]) - sum([math.sqrt(sum([(cities[newTour[(k+1) % 15]][d] - cities[newTour[k % 15]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]])) / temperature) > random.random():
# 8 		tour = copy.copy(newTour);
# 9  plt.plot(zip(*[cities[tour[i % 15]] for i in range(16) ])[0], zip(*[cities[tour[i % 15]] for i in range(16) ])[1], 'xb-', );
# 10 plt.show()
#

import random
import matplotlib.pyplot as plt


def compute_fitness(population, distance_matrix):
    fitness = 0
    for i in range(1, 8):
        fitness = fitness + distance_matrix[population[i-1]-1][population[i]-1]
    return fitness


def binary_tournament(fitness_table):
    random_number = random.randint(0, 7)
    random_number2 = random.randint(0, 7)
    if(fitness_table[random_number] > fitness_table[random_number2]):
        parent = random_number2
    else:
        parent = random_number
    return parent


def crossover(parent1, parent2):
    random_number = random.randint(0, 5)
    child = [-1, -1, -1, -1, -1, -1, -1, -1]
    child[random_number] = parent1[random_number]
    child[random_number+1] = parent1[random_number+1]
    index = random_number+2
    parent_index = index
    while(index != random_number):
        if((parent2[parent_index] in child) == False):
            child[index] = parent2[parent_index]
            index = (index + 1) % 8
        parent_index = (parent_index + 1) % 8
    return child


def mutation(child):
    random_number = random.randint(0, 7)
    random_number2 = random.randint(0, 7)
    a = child[random_number]
    child[random_number] = child[random_number2]
    child[random_number2] = a
    return child


def truncation(fitness_table, population):
    for k in range(0, 10):
        population.pop(fitness_table.index(max(fitness_table)))
        fitness_table.pop(fitness_table.index(max(fitness_table)))
    return fitness_table, population


# i have used  the same table as given in the slides
distance_matrix = list()
distance_matrix.append([0, 8, 3, 1, 4, 9, 3, 6])
distance_matrix.append([8, 0, 5, 10, 11, 4, 3, 6])
distance_matrix.append([3, 5, 0, 8, 7, 1, 5, 12])
distance_matrix.append([1, 10, 8, 0, 9, 11, 6, 4])
distance_matrix.append([4, 11, 7, 9, 0, 5, 17, 3])
distance_matrix.append([9, 4, 1, 11, 5, 0, 4, 1])
distance_matrix.append([3, 3, 5, 6, 17, 4, 0, 7])
distance_matrix.append([6, 6, 12, 4, 3, 1, 7, 0])
print("distance matrix")
print(distance_matrix)
print()

population = list()
fitness_table = list()

for i in range(0, 10):
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(a)
    population.append(a)
    fitness = compute_fitness(a, distance_matrix)
    fitness_table.append(fitness)

print("Initial population")
print(population)
print()
print("initial fitness table")
print(fitness_table)
print()

for generation in range(0, 100):

    parent1 = population[binary_tournament(fitness_table)]
    parent2 = population[binary_tournament(fitness_table)]
    parent3 = population[binary_tournament(fitness_table)]
    parent4 = population[binary_tournament(fitness_table)]
    parent5 = population[binary_tournament(fitness_table)]
    parent6 = population[binary_tournament(fitness_table)]
    parent7 = population[binary_tournament(fitness_table)]
    parent8 = population[binary_tournament(fitness_table)]
    parent9 = population[binary_tournament(fitness_table)]
    parent10 = population[binary_tournament(fitness_table)]

    child1 = crossover(parent1, parent2)
    child2 = crossover(parent2, parent1)
    child3 = crossover(parent3, parent4)
    child4 = crossover(parent4, parent3)
    child5 = crossover(parent5, parent6)
    child6 = crossover(parent6, parent5)
    child7 = crossover(parent7, parent8)
    child8 = crossover(parent8, parent7)
    child9 = crossover(parent9, parent10)
    child10 = crossover(parent10, parent9)

    child1 = mutation(child1)
    child2 = mutation(child2)
    child3 = mutation(child3)
    child4 = mutation(child4)
    child5 = mutation(child5)
    child6 = mutation(child6)
    child7 = mutation(child7)
    child8 = mutation(child8)
    child9 = mutation(child9)
    child10 = mutation(child10)

    population.append(child1)
    population.append(child2)
    population.append(child3)
    population.append(child4)
    population.append(child5)
    population.append(child6)
    population.append(child7)
    population.append(child8)
    population.append(child9)
    population.append(child10)

    for i in range(10, 20):
        fitness = compute_fitness(population[i], distance_matrix)
        fitness_table.append(fitness)

    fitness_table, population = truncation(fitness_table, population)

    print("Generation")
    print(generation)
    print("Population")
    print(population)
    print("Fitness table")
    print(fitness_table)

    plt.plot(generation, fitness_table)
