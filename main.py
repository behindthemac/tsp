from tsp import TSP


def main():
    n = 10

    tsp = TSP(n)

    shortest_route = tsp.get_shortest_route()

    tsp.show_route(shortest_route)


if __name__ == '__main__':
    main()
