from numpy import random

DEF_COST_GRAPH = [
    [0, 1139, 2373,  264, 2087,  437, 1859, 1526,  575, 1057],
    [415,    0,  861, 1956, 1571,  106, 1489, 2341,  179, 2370, ],
    [1094, 2262,    0, 1925,  601,  554,  402, 1491, 2365, 2419, ],
    [1952, 1582,  412,    0, 2468, 1517,  910,  926, 1012, 2255, ],
    [363,  317, 2211, 1954,    0, 2019, 1856, 1377, 1796,  463, ],
    [1956, 1214, 1479,  396,  729,    0, 1740, 2099, 1862, 2249, ],
    [1473, 1099, 2308, 1357, 1357, 1608,    0, 1883, 1984, 2257, ],
    [108,  618, 1397,  702, 1152,  363, 1436,    0,  602,  195, ],
    [2234,  176,  872, 2492,  950, 1624, 1513, 2308,    0, 1551, ],
    [194,  388, 2200, 1785,  505, 2024, 1162, 2089,  418,    0, ],
]


class TSP:
    # Constructor
    def __init__(self, n_cities=10, home=0, cost_graph=DEF_COST_GRAPH):
        self.n_cities = n_cities

        # Check if home is legal
        if not self.legal_home(home):
            exit()
        self.home = home

        # Check if cost_graph is legal
        if not self.legal_cost_graph(cost_graph):
            exit()
        self.cost_graph = cost_graph

    # Set number of cities and create a cost_graph
    def set_n_cities(self, n_cities):
        self.n_cities = n_cities
        self.random_cost_graph()

    # Set new cost_graph
    def set_cost_graph(self, cost_graph):
        # Check if cost_graph is legal
        if not self.legal_cost_graph(cost_graph):
            exit()

        self.cost_graph = cost_graph

    # Set new home city
    def set_home(self, home):
        # Check if home is legal
        if not self.legal_home(home):
            exit()

        self.home = home

    # Create a cost_graph with random costs
    def random_cost_graph(self):
        self.cost_graph = random.randint(low=100, high=2500, size=(
            self.n_cities, self.n_cities))

        # Assign cost_graph[n][n] to 0
        for i in range(self.n_cities):
            self.cost_graph[i][i] = 0

    # Function to check the legality of home
    def legal_home(self, home):
        # Check if home is out of bounds
        if home >= self.n_cities:
            print("Index is too big!")
            print("Please make sure it's below n_cities.")
            return False

        return True

    # Function to check the legality of cost_graph
    def legal_cost_graph(self, cost_graph):
        # Check if row and column of the array don't have the same length as number of cities
        if len(cost_graph) != self.n_cities or len(cost_graph[0]) != self.n_cities:
            print("Your cost_graph doesn't meet the requirements!")
            print("Please make sure the size of an array matches number of cities.")
            return False

        # Check if cost of cost_graph[n][n] is not 0
        for i in range(self.n_cities):
            if cost_graph[i][i] != 0:
                print("Your cost_graph doesn't meet the requirements!")
                print("Please make sure cost_graph[n][n] == 0.")
                return False

        return True
