from os import system
from time import perf_counter

from TSP import TSP
from RRHC import RRHC
from SA import SA


def cool_table_print(list_to_print):
    # Clear terminal and print table again with new values
    system("clear")  # You can remove this line if you want
    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(
        'Cost Graph', '| Algorithm', '| Time', '| Opened Nodes', '| Cost', '| Path length', '| Path'))

    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} \n".format(
        '#', '| name', '| seconds', '| #', '| $', '| #', '| []'))

    for l in list_to_print:
        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(l["gn"],
              "| " + l["a"], "| " + str(round(l["t"], 10)), "| " + str(l["on"]), "| $" + str(l["c"]), "| " + str(len(l["p"])), "| " + str(l["p"])))


def test(graphs):
    # Init tsp
    tsp = TSP()
    algorithms = [RRHC, SA]
    list_to_print = []
    graph_n = 0 # this is just a counter for cool_table_print

    # Execute each algorithm on each graph 5 times
    for graph in graphs:
        graph_n += 1
        graph_n_str = str(graph_n)
        for algorithm in algorithms:
            for _ in range(5):
                # Copy n_cities, home, and cost_graph
                tsp.set_n_cities(graph["n_cities"])
                tsp.set_home(graph["home"])
                tsp.set_cost_graph(graph["cost_graph"])

                # Start timer
                start_t = perf_counter()
                # Execute algorithm; get solution node and number of opened nodes
                solution, opened_nodes = algorithm(tsp)
                stop_t = perf_counter()
                
                # Print cool table 
                list_to_print.append({"on": opened_nodes, "gn": graph_n_str,"a": algorithm.__name__, "t": stop_t - start_t, "p": solution["path"], "c": solution["cost"]})
                cool_table_print(list_to_print)
                graph_n_str = ""
