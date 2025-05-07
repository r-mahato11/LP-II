import heapq

def a_star(start, goal, grid):
    # Manhattan distance heuristic function
    def h(x, y):
        return abs(x - goal[0]) + abs(y - goal[1])

    # List of possible movements (up, down, left, right)
    def neighbors(x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        return [(x + dx, y + dy) for dx, dy in directions if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 0]

    # Priority queue (min-heap)
    open_list = [(0 + h(*start), 0, start)]  # (f_score, g_score, (x, y))
    g_score = {start: 0}  # g(x) = cost from start to node
    came_from = {}  # To reconstruct the path

    while open_list:
        # Pop the node with the lowest f_score
        _, g, current = heapq.heappop(open_list)
        # If we reach the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return the path from start to goal

        # Explore the neighbors
        for nx, ny in neighbors(*current):
            tentative_g = g + 1  # Assume uniform cost (1 per step)
            
            # If this path is better, record it
            if (nx, ny) not in g_score or tentative_g < g_score[(nx, ny)]:
                came_from[(nx, ny)] = current
                g_score[(nx, ny)] = tentative_g
                f_score = tentative_g + h(nx, ny)
                heapq.heappush(open_list, (f_score, tentative_g, (nx, ny)))

    return None  # No path found

# Example grid and start/goal for 4x4 grid
grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

start = (0, 1)  # Starting point
goal = (3,2)   # Goal point

# Find the path using A*
path = a_star(start, goal, grid)

# Output the result
if path:
    print("Path found:", path)
else:
    print("No path found.")

