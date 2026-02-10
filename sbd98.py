#DFS depth first search
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


print("DFS Program")

# ---- input in the middle ----
n = int(input("Enter number of nodes: "))
graph = {}

for i in range(n):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter starting node: ")

# ---- DFS call ----
visited = set()
print("DFS Traversal:", end=" ")
dfs(graph, start_node, visited)
