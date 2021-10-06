# CSCE A405 Assignment 2
# Authors: Vadim Egorov and Jared Vitug
# Update date: 10/05/2021

from test_samples import GRAPHS
from test import test
# from TSP import TSP
# from RRHC import RRHC
# from SA import SA

def main():
    # tsp = TSP()
    # tsp.set_n_cities(10)
    # tsp.set_cost_graph(GRAPHS[0]["cost_graph"])

    # print(tsp.home)
    # print(tsp.cost_graph)

    # optimal_solution_anneal, _ = SA(tsp)
    # optimal_solution_rrhc, _ = RRHC(tsp)

    # print("RRHC optimal solution path: ", optimal_solution_rrhc["path"])
    # print("RRHC optimal solution cost: ", optimal_solution_rrhc["cost"])

    # print("SA optimal solution path: ", optimal_solution_anneal["path"])
    # print("SA optimal solution cost: ", optimal_solution_anneal["cost"])

    print("---Test Started---")
    test(GRAPHS)
    print("----Test Ended----")

    return


if __name__ == "__main__":
    main()
