import heapq

graph = {
    "a": [("b", 3), ("c", 2)],
    "b": [("e", 4), ("d", 1)],
    "c": [("e", 2), ("d", 5)],
    "d": []
}

def uniformCostSearch(start, goal, graph):
    frontier = [(0, [start])]

    while frontier:
        cost, path = heapq.heappop(frontier)
        visited = set()
        current = path[-1]

        if current == goal:
            return current, cost, path

        if current in visited:
            continue

        for neighbor, succCost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(frontier, (cost + succCost, path + [neighbor]))


print(uniformCostSearch("a", "d", graph))