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
    bfs_path = np.array([])
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

    next_index = np.array([bfs_goal[0], bfs_goal[1]])
    while pathfinding:
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        smallest = float('inf')  # Initialize smallest with positive infinity
        index = next_index
        print(index)
        for i in range(8):
            new_x = index[1] + dx[i]
            new_y = index[0] + dy[i]
            # Ensure coordinates are within bounds of the matrix
            if 0 <= new_x < m_cols and 0 <= new_y < m_rows:
                value = search[new_y, new_x]
                # Update minimum if found a smaller value that is not zero
                if value != 0 and value < smallest:
                    smallest = value
                    next_index = np.array([new_y, new_x])
                    if smallest == 1:
                        np.append(bfs_path, start)
                        pathfinding = False
                        continue
        np.append(bfs_path, index)

    print(bfs_path)

    plt.figure()
    plt.imshow(search, cmap='binary', interpolation='nearest')
    plt.plot(bfs_path[:, 1], bfs_path[:, 0], marker='o', color='red')
    plt.show()

    return bfs_path


# plt.imshow(map, cmap='binary', interpolation='nearest')
# plt.show()

bfs(map, goal, start)
