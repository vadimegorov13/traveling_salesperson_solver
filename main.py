from TSP import TSP


def main():
    travel_map = TSP()

    travel_map.set_n_cities(7)
    travel_map.set_home(2)

    print(travel_map.home)
    print(travel_map.cost_graph)

    return


if __name__ == "__main__":
    main()
