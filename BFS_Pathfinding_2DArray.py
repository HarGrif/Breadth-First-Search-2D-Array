import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt


'''
This function performs a Breadth-First Search of a 2D array to find the shortest path between the start and the goal.

It takes inputs in the form of start coordinates, goal coordinates and a 2D map in the form of an array wit 0 as empty
space and 1 for obstacles.

It returns a boolean term to show if the map is solvable, and if the map is solvable returns the shortest path.

MIT License

Copyright (c) 2024 HarGrif

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''


def bfs(bfs_map, bfs_goal, bfs_start):
    solvable = True
    solving = True
    pathfinding = True
    bfs_path = []
    m_rows = len(bfs_map)
    m_cols = len(bfs_map[0])

    # Initialise search point
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

            # Check indices are within matrix bounds

            # For cell to the left
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
        if np.array_equal(search, prev_step):
            solvable = False
            solving = False
        if search[bfs_goal[0], bfs_goal[1]] == 0:
            continue
        solving = False

    if solvable:
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
    else:
        fin_path = None

    plt.figure()
    plt.imshow(search, cmap='viridis', interpolation='nearest')
    plt.colorbar()

    return fin_path, solvable
