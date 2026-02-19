#cycle detection
def dfs(node, parent, visited, graph):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, node, visited, graph):
                return True
        elif neighbor != parent:
            return True

    return False


def has_cycle(graph):
    visited = set()

    for node in graph:
        if node not in visited:
            if dfs(node, -1, visited, graph):
                return True

    return False


# Example graph (cycle exists)
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

print("Cycle detected" if has_cycle(graph) else "No cycle")
