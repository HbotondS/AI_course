import numpy as np
import sys
from tables import three_by_three
from tables import five_by_five

grid = three_by_three
cell_size = 3

print(np.matrix(grid))
print('---------------')


def possible(y, x, n):
    global grid
    for i in range(len(grid)):
        if grid[y][i] == n:
            return False

    for i in range(len(grid)):
        if grid[i][x] == n:
            return False

    x0 = (x//cell_size) * cell_size
    y0 = (y//cell_size) * cell_size
    for i in range(cell_size):
        for j in range(cell_size):
            if grid[y0+i][x0+j] == n:
                return False

    return True


def solve():
    global grid
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == 0:
                for n in range(1, 26):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    sys.exit()

solve()