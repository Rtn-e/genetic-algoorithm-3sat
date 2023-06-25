import sys
import CNFChecker
import numpy as np
import random
import math

mycnf = CNFChecker('Input.cnf')
print (mycnf.count_number_of_satisfactions())

def fitness (evalCNF) :
    global mycnf
    return mycnf.count_number_of_satisfactions(evalCNF))
def toCNF (evalCNF) :
    for i in range (len(evalCNF)) :
        if (evalCNF[i] == 1) :
            return i + 1
        else:
            return -i - 1
