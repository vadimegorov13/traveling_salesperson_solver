from random import randrange
from math import exp
from numpy.random.mtrand import rand

from helper_functions import get_neighbors, random_restart

MAX_STEPS = 100
START_TEMP = 100

# Simulated annealing function
def SA(tsp):
    opened_nodes = 0
    # Get random path
    curr_best = random_restart(tsp)
    curr_node = curr_best

    # Iterate MAX_STEPS times (1000)
    for i in range(MAX_STEPS):
        # Get all neighbors
        neighbors, opened_nodes = get_neighbors(tsp.cost_graph, curr_node["path"], opened_nodes)
        
        # Get random neighbor
        potential_neighbor = neighbors[randrange(len(neighbors))]

        # Check if cost of random neighbor is lower than cost of current best solution
        if potential_neighbor["cost"] < curr_best["cost"]:
            curr_best = potential_neighbor

        # Get delta E
        change_energy = abs(potential_neighbor["cost"] - curr_best["cost"])
        # Get temperature
        curr_temp = START_TEMP / float(i + 1)
        # Get accuracy rate
        acc_rate = exp(-change_energy / curr_temp)

        # Check if delta E less than 0 or accuracy rate greater than random number (from 0 to 1)
        if change_energy < 0 or rand() < acc_rate:
            curr_node = potential_neighbor

    return curr_best, opened_nodes