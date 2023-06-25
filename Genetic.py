import sys
from CNFChecker import CNFChecker
import numpy as np
from random import *
import math

class Genetic:
    def __init__(self, gene: list):
        self.gene = gene
        self.fitness = fitness(gene)
def fitness (evalCNF) :
    return mycnf.count_number_of_satisfactions(evalCNF)
def toCNF (evalCNF) :
    print("[", end="")
    for i in range (len(evalCNF)) :
        if (evalCNF[i] == 1) :
            print(i + 1, end=", ")
        else:
            print(-(i + 1), end = ", ")
    print("]")

mycnf = CNFChecker('Input.cnf')
populate = mycnf.nv
parent_num = int(math.sqrt(populate))
'print(populate)'


def choose_parent(people):
    #parent % : 90% from best , 10% from bads
    top = int(parent_num * 0.9)
    bottom = parent_num - top
    new = []
    for i in range(0, bottom) :
        new.append(people[i])
    for i in range (len(people) - top, len(people)):
        new.append(people[i])
    return new


def mutate(child):
    #mutation % : 85%
    p = randint(0, 100)
    if p <= 85:
        random_index = randint(0, mycnf.nv - 1)
        child[random_index] ^= 1
    child = Genetic(child)
    return child
        

def cross_over(parent1, parent2):
    index = randint(0, mycnf.nv)
    gene = []
    for i in range (index) :
        gene.append(parent1.gene[i])
    for i in range (index, mycnf.nv):
        gene.append(parent2.gene[i])
    return mutate(gene)

def make_children (parent_list, generation_list) :
    for i in range(parent_num):
        parent1 = parent_list[i]
        for j in range(parent_num):
            if i != j:
                parent2 = parent_list[j]
                child = cross_over(parent1, parent2)
                generation_list.append(child)
    return choosing_survivers(parent_list, generation_list)
    
def choosing_survivers(parent_list, generation_list):
    generation_list.sort(key=lambda x: x.fitness)
    top = int(parent_num * 0.9)
    bottom = parent_num - top
    new = []
    for i in range(0, bottom) :
        new.append(generation_list[i])
    for i in range (len(generation_list) - top, len(generation_list)):
        new.append(generation_list[i])
    return new

generation = []
for i in range(parent_num) :
    generation.append(Genetic(np.random.choice([0, 1], size=mycnf.nv)))
generation.sort(key=lambda x: x.fitness)
parent = []
for k in range(1000):
    print(f'{k}omin bar meghdar maximum => {generation[-1].fitness}')
    parent = choose_parent(generation)
    generation = make_children(parent, generation)
    if generation[-1].fitness == mycnf.clauses_size:
        break
print(f'behtarin meghdar {generation[-1].fitness}\n CNF :')
toCNF(generation[-1].gene)
