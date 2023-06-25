from pysat.formula import CNF
import numpy as np

class CNFChecker :
    def __init__(self, path):
    self.positive_contribution = {}
    self.negative_contribution = {}
    self.cnf = CNF(from_file=path)
    self.nv = self.cnf.nv
    self.clauses_size = len(self.cnf.clauses)
    for i, clause in enumerate(self.cnf.clauses):
        for variable in clause:
            if variable > 0:
                self.positive_contribution.setdefault(variable, set()).add(i)
            else:
                self.negative_contribution.setdefault(-variable, set()).add(i)
    def count_number_of_satisfactions(self, cnf_evaluation):
    result = 0
    satisfied_parts = set()
    for i in range(self.clauses_size):
        clause = self.cnf.clauses[i]
        for literal in clause:
            if (literal > 0 and cnf_evaluation[literal-1]) or (literal < 0 and not cnf_evaluation[abs(literal)-1]):
                satisfied_parts.add(i)
                result += 1
                break
    return result
