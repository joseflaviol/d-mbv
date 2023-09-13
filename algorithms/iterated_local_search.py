from typing import Callable, List, Tuple
from random import uniform
import time

class IteratedLocalSearch:

    def __init__(self, objective: Callable, generate_initial_solution: Callable, local_search: Callable, operators: List[Tuple[Callable, float]], minimize: bool = True):
        self.objective                 = objective
        self.generate_initial_solution = generate_initial_solution
        self.local_search              = local_search
        self.operators                 = operators
        self.minimize                  = minimize
    
    def compare(self, x, y):
        return (self.minimize and x < y) or (not(self.minimize) and x > y)

    def iterate(self):
        initial = self.generate_initial_solution()
        current = self.local_search(initial)

        initial_o = self.objective(initial)
        current_o = self.objective(current)

        if self.compare(initial_o, current_o):
            best_s = initial
            best_o = initial_o
        else:
            best_s = current
            best_o = current_o

        starting_time = time.time()
        while time.time() < starting_time + 10:
            operator = self.select_operator()

            perturbed    = operator(current)
            perturbed_ls = self.local_search(perturbed)

            perturbed_o    = self.objective(perturbed)
            perturbed_ls_o = self.objective(perturbed_ls)

            print(perturbed_o, perturbed_ls_o)

            if self.compare(perturbed_ls_o, current_o):
                current   = perturbed_ls
                current_o = perturbed_ls_o
            
                if self.compare(current_o, best_o):
                    best_s = current
                    best_o = current_o

        return (best_s, best_o)

    def select_operator(self):
        rand_num = uniform(0, 1.0)

        for op, prob in self.operators:
            if rand_num <= prob:
                return op