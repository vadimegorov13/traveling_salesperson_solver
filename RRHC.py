# Random restart Hill-Climbing
from numpy import random
from copy import deepcopy
from sys import maxsize

def path_cost(cost_graph, path):
    cost = 0

    for i in range(len(path) - 1):
        cost += cost_graph[path[i]][path[i+1]]

    return cost


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


def get_neighbors(cost_graph, path, opened_nodes):
    n = len(path) - 1
    neighbors = list()

    for i in range(1, n):
        for j in range(i + 1, n):
            neighbor = deepcopy(path)
            neighbor[i] = path[j]
            neighbor[j] = path[i]
            neighbors.append(
                {"path": neighbor, "cost": path_cost(cost_graph, neighbor)})
            opened_nodes += 1

    return neighbors, opened_nodes


def optimal_neighbor(cost_graph, path, opened_nodes):
    neighbors, opened_nodes = get_neighbors(cost_graph, path, opened_nodes)
    # print("Neighbors: ", neighbors)
    optimal_neighbor = neighbors[0]
    min_cost = neighbors[0]["cost"]

    for neighbor in neighbors:
        if min_cost > neighbor["cost"]:
            min_cost = neighbor["cost"]
            optimal_neighbor = neighbor

    return optimal_neighbor, opened_nodes


def hill_climbing(tsp, opened_nodes):
    curr_node = random_restart(tsp)

    # print("Starting path: ", curr_node["path"])
    # print("Starting cost: ", curr_node["cost"])

    while True:
        neighbor, opened_nodes = optimal_neighbor(tsp.cost_graph, curr_node["path"], opened_nodes)

        # print("Optimal neighbor path: ", neighbor["path"])
        # print("Optimal neighbor cost: ", neighbor["cost"])

        if neighbor["cost"] >= curr_node["cost"]:
            return curr_node, opened_nodes

        curr_node = neighbor


def RRHC(tsp):
    opened_nodes = 0
    optimal_solution = {"path": [], "cost": maxsize}

    for _ in range(100):
        optimal_node, opened_nodes = hill_climbing(tsp, opened_nodes)

        # print("Optimal node path: ", optimal_node["path"])
        # print("Optimal node cost: ", optimal_node["cost"])

        if optimal_solution["cost"] >= optimal_node["cost"]:
            optimal_solution = optimal_node
            
    return optimal_solution, opened_nodes
