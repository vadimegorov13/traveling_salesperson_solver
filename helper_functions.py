# This file contains functions that are used in both SA and RRHC
# (It's just to keep our code DRY)

from numpy import random
from copy import deepcopy


# Get cost of the path
def path_cost(cost_graph, path):
    cost = 0

    # Iterate through the path and count the cost
    for i in range(len(path) - 1):
        cost += cost_graph[path[i]][path[i+1]]
    return cost


# Generate random path
def random_restart(tsp):
    # Create list of cities
    cities = list(range(tsp.n_cities))
    path = list()

    # Remove home city from the list
    cities.remove(tsp.home)

    # Itirate n_cities - 1 times
    for _ in range(tsp.n_cities - 1):

        # Randomly get a city from the list of cities
        rand_city = cities[random.randint(0, len(cities))]

        # Add rand_city to the path and remove it from the list of cities
        path.append(rand_city)
        cities.remove(rand_city)

    # Add home city to the front and back of the path list
    path.insert(0, tsp.home)
    path.append(tsp.home)

    return {"path": path, "cost": path_cost(tsp.cost_graph, path)}


# Get all neighbors
def get_neighbors(cost_graph, path, opened_nodes):
    n = len(path) - 1
    neighbors = list()

    # Iterate through the path excluding first and last indexes (home city)
    for i in range(1, n):
        for j in range(i + 1, n):
            # Copy path and then switch cities on i and j
            neighbor = deepcopy(path)
            neighbor[i] = path[j]
            neighbor[j] = path[i]
            # Append new neighbor to the list
            neighbors.append(
                {"path": neighbor, "cost": path_cost(cost_graph, neighbor)})
            opened_nodes += 1

    return neighbors, opened_nodes
