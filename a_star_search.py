import heapq
import math

graph = {
    "A": [("B", 2)],
    "B": [("A", 2), ("C", 2)],
    "C": [("B", 2), ("D", 1)],
    "D": [("C", 1), ("E", 1)],
    "E": []
}

coordinates = {
    "A": (0, 0),
    "B": (1, 0),
    "C": (2, 0),
    "D": (3, 0),
    "E": (4, 0)
}

def euclidean_heuristic(a, b, coordinates):
    x1, y1 = coordinates[a]
    x2, y2 = coordinates[b]

    return math.sqrt(((y1 - y2) ** 2) + ((x1 - x2) ** 2))


def a_star_search(start, goal, graph, coords, heuristic):
    initial_heuristic = heuristic(start, goal, coords)
    frontier = [(initial_heuristic, 0, [start])]
    visited = set()

    while frontier:
        f, g, path = heapq.heappop(frontier)
        current = path[-1]

        if current == goal:
            return g, path

        if current in visited:
            continue

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                g_prime = g + cost
                h_cost = heuristic(neighbor, goal, coords)
                f_score = g_prime + h_cost
                heapq.heappush(frontier, (f_score, g_prime, path + [neighbor]))

    return None, float("inf")

g, path = a_star_search("A", "E", graph, coordinates, euclidean_heuristic)
print(g,path)