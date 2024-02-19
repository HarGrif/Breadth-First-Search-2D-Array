import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

map = np.zeros([25, 30])
map[20, 0:10] = 1
map[20, 19:30] = 1
map[8, 4:20] = 1
map[9:25, 16] = 1
start = np.array([24, 1])
goal = np.array([24, 29])


def bfs(bfs_map, bfs_goal, bfs_start):
    solving = True
    pathfinding = True
    m_rows = len(bfs_map)
    m_cols = len(bfs_map[0])
    search = np.zeros([m_rows, m_cols])
    search[bfs_start[0], bfs_start[1]] = 1
    step = 0
    while solving:
        step += 1
        prev_step = deepcopy(search)
        # Finds index of squares with same number as step
        indices = np.where(search == step)
        # Iterates through all the found squares
        for i in range(len(indices[0])):
            index = np.array([indices[0][i], indices[1][i]])

            # For cell to the left
            # Check if the indices are within the bounds of the matrix
            if 0 <= index[0] - 1 < m_rows and 0 <= index[1] < m_cols:
                # Check if squares have been stepped on before or if the map has an obstacle there
                if search[index[0] - 1, index[1]] == 0 and bfs_map[index[0] - 1, index[1]] == 0:
                    # Take step
                    search[index[0] - 1, index[1]] = step + 1

            # For cell to the right
            if 0 <= index[0] + 1 < m_rows and 0 <= index[1] < m_cols:
                # Check if squares have been stepped on before or if the map has an obstacle there
                if search[index[0] + 1, index[1]] == 0 and bfs_map[index[0] + 1, index[1]] == 0:
                    # Take step
                    search[index[0] + 1, index[1]] = step + 1

            # For cell above
            if 0 <= index[0] < m_rows and 0 <= index[1] - 1 < m_cols:
                # Check if squares have been stepped on before or if the map has an obstacle there
                if search[index[0], index[1] - 1] == 0 and bfs_map[index[0], index[1] - 1] == 0:
                    # Take step
                    search[index[0], index[1] - 1] = step + 1

            # For cell below
            if 0 <= index[0] < m_rows and 0 <= index[1] + 1 < m_cols:
                # Check if squares have been stepped on before or if the map has an obstacle there
                if search[index[0], index[1] + 1] == 0 and bfs_map[index[0], index[1] + 1] == 0:
                    # Take step
                    search[index[0], index[1] + 1] = step + 1

        if search[bfs_goal[0], bfs_goal[1]] == 0:
            continue
        solving = False
        if np.array_equal(search, prev_step):
            bfs_path = None
            print("Unsolvable")

    plt.imshow(search, cmap='binary', interpolation='nearest')
    plt.show()

    return bfs_path


plt.imshow(map, cmap='binary', interpolation='nearest')
plt.show()

bfs(map, goal, start)

#just for the commit