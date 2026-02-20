#shortest path in grid
from collections import deque

def shortestPath(grid):
    rows = len(grid)
    cols = len(grid[0])

    #start or end is blocked
    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return -1

    queue = deque([(0, 0, 1)])  # (row, col, distance)
    grid[0][0] = 1  # mark visited

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c, dist = queue.popleft()

        #reached destination
        if r == rows - 1 and c == cols - 1:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                grid[nr][nc] = 1  # mark visited
                queue.append((nr, nc, dist + 1))

    return -1  # no path found

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]

print(shortestPath(grid))
