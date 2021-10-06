from numpy import random
from random import randrange
from copy import deepcopy
from sys import maxsize
from math import exp

from numpy.random.mtrand import rand

MAX_STEPS = 100
START_TEMP = 1000

def random_restart(tsp):
    cities = list(range(tsp.n_cities))
    path = list()
    cities.remove(tsp.home)

    for _ in range(tsp.n_cities - 1):
        rand_city = cities[random.randint(0, len(cities))]
        path.append(rand_city)
        cities.remove(rand_city)

    path.insert(0, tsp.home)
    path.append(tsp.home)

    return {"path": path, "cost": path_cost(tsp.cost_graph, path)}


def path_cost(cost_graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += cost_graph[path[i]][path[i + 1]]
    return cost


def get_neighbors(cost_graph, path, opened_nodes):
    n = len(path) - 1
    neighbors = list()

    for i in range(1, n):
        for j in range(i + 1, n):
            neighbor = deepcopy(path)
            neighbor[i] = path[j]
            neighbor[j] = path[i]
            neighbors.append(
                {"path": neighbor, "cost": path_cost(cost_graph, neighbor)}
            )
            opened_nodes += 1

    return neighbors, opened_nodes


def SA(tsp):
    opened_nodes = 0
    curr_node = random_restart(tsp)
    optimal_solution = {"path": [], "cost": maxsize}

    for i in range(MAX_STEPS):
        neighbors, opened_nodes = get_neighbors(tsp.cost_graph, curr_node["path"], opened_nodes)
        curr_best = neighbors[0]
        curr_best_cost = neighbors[0]["cost"]

        curr_node, curr_node_cost = curr_best, curr_best_cost

        rand_neighbor = randrange(len(neighbors))
        potential_neighbor = neighbors[rand_neighbor]
        potential_neighbor_cost = neighbors[rand_neighbor]["cost"]

        if potential_neighbor_cost < curr_best_cost:
            curr_best, curr_best_cost = potential_neighbor, potential_neighbor_cost

        change_energy = abs(potential_neighbor_cost - curr_node_cost)
        curr_temp = START_TEMP / float(i + 1)
        acc_rate = exp(-change_energy / curr_temp)

        # print()
        # print("step:         ", i)
        # print("change_energy:", change_energy)
        # print("curr_temp:    ", curr_temp)
        # print("acc_rate:     ", acc_rate)

        if change_energy < 0 or rand() < acc_rate:
            
            # print()
            # print("change")
            # print("step:         ", i)
            # print("change_energy:", change_energy)
            # print("curr_temp:    ", curr_temp)
            # print("acc_rate:     ", acc_rate)

            curr_node, curr_node_cost = potential_neighbor, potential_neighbor_cost

    optimal_solution["path"] = curr_best["path"]
    optimal_solution["cost"] = curr_best_cost

    return optimal_solution, opened_nodes
