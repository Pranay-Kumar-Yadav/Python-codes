#topological sort
def dfs(node, visited, stack, graph):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, stack, graph)

    stack.append(node)


def topological_sort(graph):
    visited = set()
    stack = []

    for node in graph:
        if node not in visited:
            dfs(node, visited, stack, graph)

    return stack[::-1]


# Example DAG
graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    1: [],
    0: []
}

print("Topological Order:", topological_sort(graph))

