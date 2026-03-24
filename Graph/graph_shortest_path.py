
from collections import deque

def shortest_path(graph, start, end):
    # if start equals end
    if start == end:
        return 0, [start]

    visited = set([start])
    queue = deque([(start, [start])])  # (node, path)

    while queue:
        node, path = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor == end:
                final_path = path + [neighbor]
                distance = len(final_path) - 1
                return distance, final_path

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return -1, []  # if not reachable


# Graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

# Run
distance, path = shortest_path(graph, "A", "F")

print("Distance:", distance)
print("Path:", path) 

 