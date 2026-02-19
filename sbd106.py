#dijkstra's algorithm
import heapq

def dijkstra(graph, start):
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue (min heap)
    min_heap = [(0, start)]  # (distance, node)

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        # Skip if already visited with shorter distance
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Relaxation step
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances


#  Graph (Adjacency List)
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

start_node = int(input("Enter start node: "))

shortest_distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node)
for node in shortest_distances:
    print(f"{node} : {shortest_distances[node]}")
