import numpy as np
import matplotlib.pyplot as plt
from BFS_Pathfinding_2DArray import bfs

# Initialise map parameters for a solvable map
map = np.zeros([25, 30])
map[20, 0:10] = 1
map[20, 19:30] = 1
map[8, 4:20] = 1
map[9:25, 16] = 1
start = np.array([24, 1])
goal = np.array([24, 29])

# Run the BFS for both maps
path, solvable = bfs(map, goal, start)

# Check if path was found
if solvable:
    # Plot map, path, start and goal
    plt.figure()
    plt.imshow(map, cmap='gray', interpolation='nearest')
    plt.plot(path[1, :], path[0, :], marker='o', color='red', label='Path')
    plt.plot(start[1], start[0], marker='^', color='green', label='Start')
    plt.plot(goal[1], goal[0], marker='v', color='green', label='Goal')
    plt.legend()
else:
    # Plot map, start and goal
    print("Map 1 is unsolvable")
    plt.figure()
    plt.imshow(map, cmap='gray', interpolation='nearest')
    plt.plot(start[1], start[0], marker='^', color='green', label='Start')
    plt.plot(goal[1], goal[0], marker='v', color='green', label='Goal')
    plt.legend()

plt.show()
