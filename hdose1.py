import numpy as np
from collections import deque
def write_obstacles_to_file(file_name):
    print("Enter obstacle positions in format: North East South West")

    with open(file_name, "w") as file:
        while True:
            data = input("Enter obstacle positions: ")
            if data.lower() == "done":
                break
            file.write(data + "\n")
    
    print(f"\nObstacles saved to {file_name}!\n")

def create_arena(file_name, n):
    # Initialize n × n matrix with 1s 
    arena = np.ones((n, n), dtype=int)

    # Read obstacles from file
    with open(file_name, "r") as file:
        for line in file:
            try:
                north, east, south, west = map(int, line.strip().split())

                # Place obstacles
                if 0 <= north < n:  arena[north][0] = 0  
                if 0 <= east < n:   arena[0][east] = 0   
                if 0 <= south < n:  arena[south][n-1] = 0  
                if 0 <= west < n:   arena[n-1][west] = 0  

            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")

    return arena


def bfs_shortest_path(arena, start, goal):
    n = len(arena)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    queue = deque([(start, [start])])  
    visited = set([start])  

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path  # Return the shortest path if goal is reached

        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # New position

            if 0 <= nx < n and 0 <= ny < n and arena[nx][ny] == 1 and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

file_name = "obstacles.txt"

# Write obstacles to file
write_obstacles_to_file(file_name)

# Define arena size
n = int(input("\nEnter arena size (n × n): "))

# Generate and display the arena
arena = create_arena(file_name, n)
print("\nArena Map:")
print(arena)

x = int(input("Enter the x-final corrdinate "))
y = int(input("Enter the y-final coordinate "))
start = (0, 0)
goal = (x, y)
path = bfs_shortest_path(arena, start, goal)

if path:
    print("\nShortest Path Found:")
    print(" -> ".join(str(step) for step in path))
else:
    print("\nNo path found to the destination.")
