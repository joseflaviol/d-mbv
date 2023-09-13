from graph.graph_class                import Graph
from npe.npe_class                    import NPE
from npe.operators                    import sprn
from algorithms.simulated_annealing   import SimulatedAnnealing
from algorithms.iterated_local_search import IteratedLocalSearch
from typing                           import Callable
import random

g = Graph(10)

for i in range(g.number_of_vertices):
    for j in range(i + 1, g.number_of_vertices):
        g.add_edge(i, j)

print('gerou')

def objective(npe: NPE, d):
    degree = [0]    * len(npe.n)
    roots  = [None] * len(npe.n)

    roots[0] = npe.n[0]
    j        = 1

    while j < len(npe.n):
        k                = roots[npe.d[j] - 1]
        degree[k]        = degree[k] + 1
        degree[npe.n[j]] = degree[npe.n[j]] + 1
        roots[npe.d[j]]  = npe.n[j]
        j                = j + 1

    cont = 0

    for v in degree:
        if v > d:
            cont += 1
    
    return cont

# Create a lambda function that only takes x (npe) as an argument
objective_function = lambda x: objective(x, d = 2)

'''
npe = NPE(g)
print(objective(npe, 2))

sa = SimulatedAnnealing(npe, 20, 0.99, [(sprn, 1.0)], objective_function)

x_best, f_best = sa.anneal()
'''
# ils functions
def generate_initial_solution(g: Graph):
    return NPE(g)

generate_initial_solution_function = lambda : generate_initial_solution(g = g)

def local_search(npe: NPE, operator: Callable, objective: Callable):
    initial_solution_objective = objective(npe)

    for _ in range(50):
        x_new = operator(npe)
        f_new = objective(x_new)

        if f_new < initial_solution_objective:
            return x_new

    return npe 

local_search_function = lambda x: local_search(x, operator = sprn, objective = objective_function)

ils = IteratedLocalSearch(objective = objective_function, generate_initial_solution = generate_initial_solution_function, local_search=local_search_function, operators=[(sprn, 1.0)])
x_best, f_best = ils.iterate()

print(x_best.decode(), f_best)