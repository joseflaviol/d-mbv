from typing import List, Tuple, Callable
from random import uniform
from numpy  import exp
import time

class SimulatedAnnealing:

    def __init__(self, x0, initial_temp: float, cooling_rate: float, operators: List[Tuple[Callable, float]], objective: Callable, minimize: bool = True):
        self.x0           = x0
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.operators    = sorted(operators, key = lambda x: x[1])
        self.objective    = objective
        self.minimize     = minimize
    
    def anneal(self):
        x_current = self.x0 
        f_current = self.objective(self.x0)
        T         = self.initial_temp
        x_best    = x_current
        f_best    = f_current

        f_max = f_current
        f_min = f_current

        starting_time = time.time()
        while time.time() < starting_time + 10:
            operator = self.select_operator()

            x_new = operator(x_current)
            f_new = self.objective(x_new)

            if f_new > f_max:
                f_max = f_new
            
            if f_new < f_min:
                f_min = f_new

            p_accept = exp(-(f_new - f_current) / T)  

            if uniform(0, 1.0) <= p_accept:
                x_current = x_new
                f_current = f_new

                if self.minimize and f_current < f_best:
                    x_best = x_current
                    f_best = f_current
            

            T *= self.cooling_rate
        print(f_min, f_max)
        return (x_best, f_best)

    def select_operator(self):
        rand_num = uniform(0, 1.0)

        for op, prob in self.operators:
            if rand_num <= prob:
                return op