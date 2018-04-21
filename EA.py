import random


def compute_fitness(arr, distance_matrix):
    fitness = 0
    for i in range(1, 8):
        fitness = fitness + distance_matrix[arr[i-1]-1][arr[i]-1]
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

initial_population = list()
fitness_table = list()

for i in range(0, 10):
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(a)
    initial_population.append(a)
    fitness = compute_fitness(a, distance_matrix)
    fitness_table.append(fitness)

print("Initial population")
print(initial_population)
print()
print("fitness table")
print(fitness_table)
print()

parent1 = initial_population[binary_tournament(fitness_table)]
parent2 = initial_population[binary_tournament(fitness_table)]

print("parent1")
print(parent1)
print()
print("parent2")
print(parent2)
print()

child1 = crossover(parent1, parent2)
child2 = crossover(parent2, parent1)
print("child 1")
print(child1)
print()
print("child 2")
print(child2)
print()

child1 = mutation(child1)
child2 = mutation(child2)

print(child1)
print(child2)


# def truncation(fitness_table):

