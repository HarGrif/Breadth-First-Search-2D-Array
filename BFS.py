import numpy as np
from copy import deepcopy


def bfs(bfs_map, bfs_goal, bfs_start):
    solving = True
    pathfinding = True
    bfs_path = []
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
        for i in range(8):
            new_x = index[1] + dx[i]
            new_y = index[0] + dy[i]
            # Ensure coordinates are within matrix
            if 0 <= new_x < m_cols and 0 <= new_y < m_rows:
                value = search[new_y, new_x]
                # Update minimum if smaller value found
                if value != 0 and value < smallest:
                    smallest = value
                    next_index = np.array([new_y, new_x])
                    # Check if goal start has been reached
                    if smallest == 1:
                        pathfinding = False
                        continue
        bfs_path.append(index)

    # Convert list of arrays to 2D array with format [[y1, y2, y3, ... ,yn],[x1, x2, x3, ... ,xn]]
    bfs_path.append(bfs_start)
    fin_path = np.zeros([2, len(bfs_path)])
    for i in range(len(bfs_path)):
        fin_path[0, i] = bfs_path[i][0]
        fin_path[1, i] = bfs_path[i][1]
    print(fin_path)

    return fin_path
