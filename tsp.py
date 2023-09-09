import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from permutations import circular_permutations


class TSP:
    def __init__(self, n):
        """Initializes the instance.

        Args:
            n: The number of cities
        """
        self.n = n

        self.c = np.random.rand(self.n, 2)

        self.d = self.get_distance()

    def get_distance(self):
        """Computes the distance matrix from the coordinates.

        Returns:
            The distance matrix
        """
        d = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                if i < j:
                    d[i][j] = distance.euclidean(self.c[i], self.c[j])
                elif i > j:
                    d[i][j] = d[j][i]
                else:
                    d[i][j] = 0
        return d

    def get_length(self, route):
        """Gets the length of a given route.

        Args:
            route: Indices of the cities arranged in visiting order

        Returns:
            The length of the given route
        """
        length = 0
        for i in range(self.n):
            length += self.d[route[i]][route[(i + 1) % self.n]]
        return length

    def show_route(self, route):
        """Shows the given route.

        Args:
            route: Indices of the cities arranged in visiting order
        """
        x = []
        y = []
        for i in range(self.n + 1):
            r = route[i % self.n]
            x.append(self.c[r, 0])
            y.append(self.c[r, 1])
        plt.scatter(x, y)
        plt.plot(x, y)
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.gca().set_aspect('equal')
        plt.show()

    def get_shortest_route(self):
        """Gets the shortest route.

        Returns:
            shortest_route: The shortest route
        """
        routes = circular_permutations(list(range(self.n)))

        shortest_route = next(routes)
        shortest_length = self.get_length(shortest_route)
        for route in routes:
            length = self.get_length(route)
            if length < shortest_length:
                shortest_route = route
                shortest_length = length
        return shortest_route
