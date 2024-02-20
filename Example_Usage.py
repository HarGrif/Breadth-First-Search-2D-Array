import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from BFS import bfs

# Initialise map parameters
map = np.zeros([25, 30])
map[20, 0:10] = 1
map[20, 19:30] = 1
map[8, 4:20] = 1
map[9:25, 16] = 1
start = np.array([24, 1])
goal = np.array([24, 29])

path = bfs(map, goal, start)

# Plot map, search and path
plt.figure()
plt.imshow(search, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.plot(fin_path[1, :], fin_path[0, :], marker='o', color='red')
plt.show()