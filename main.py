from test_samples import GRAPHS
from test import test

def main():
    # tsp = TSP()
    # tsp.set_n_cities(16)
    # tsp.set_cost_graph(GRAPHS[3]["cost_graph"])

    # print(tsp.home)
    # print(tsp.cost_graph)

    # optimal_solution = RRHC(tsp)

    # print("optimal solution path: ", optimal_solution["path"])
    # print("optimal solution cost: ", optimal_solution["cost"])

    print("---Test Started---")
    test(GRAPHS)
    print("----Test Ended----")

    return


if __name__ == "__main__":
    main()
