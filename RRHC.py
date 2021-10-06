# Random restart Hill-Climbing
from numpy import random
from copy import deepcopy
from sys import maxsize

from helper_functions import get_neighbors, random_restart


def optimal_neighbor(cost_graph, path, opened_nodes):
    # Get all neighbors
    neighbors, opened_nodes = get_neighbors(cost_graph, path, opened_nodes)
    # print("Neighbors: ", neighbors)
    optimal_neighbor = neighbors[0]
    min_cost = neighbors[0]["cost"]

    # Iterate through every neighbor and conpare their cost
    for neighbor in neighbors:
        if min_cost > neighbor["cost"]:
            min_cost = neighbor["cost"]
            optimal_neighbor = neighbor

    # Return neighbor with the lowes cost
    return optimal_neighbor, opened_nodes

# Hill climbing function
def hill_climbing(tsp, opened_nodes):
    # Get random path
    curr_node = random_restart(tsp)

    while True:
        # Get neighbor with the lowes cost
        neighbor, opened_nodes = optimal_neighbor(tsp.cost_graph, curr_node["path"], opened_nodes)

        # Check if the cost of neighbor is greater or equal to the cost of current node
        if neighbor["cost"] >= curr_node["cost"]:
            return curr_node, opened_nodes

        curr_node = neighbor


# Random restart hill climbing function
def RRHC(tsp):
    # Init open node counter and optimal solution
    opened_nodes = 0
    optimal_solution = {"path": [], "cost": maxsize}

    # Iterate 100 times and get the most optimal solution throughout all hill climbing solutions
    for _ in range(100):
        optimal_node, opened_nodes = hill_climbing(tsp, opened_nodes)

        # Compare optimal solution with the node from hill climbing
        if optimal_solution["cost"] >= optimal_node["cost"]:
            optimal_solution = optimal_node
            
    return optimal_solution, opened_nodes
