import copy

def create_grid(grid):
    rows, cols = (4, 4)
    grid = [[0 for x in range(cols)]for x in range(rows)]
    # grid.insert(0, grind)
    return grid


def print_grid(grid):
    for r in grid:
        for c in r:
            print(c, end=" " * 5)
        print()

def check_lost(grid):
    for r in grid:
        len_r = len(r)
        for v in range(len_r):
            next_v = v + 1
            if r[v] == 0:
                return False
            if not (next_v > len_r - 1):
                if r[v] == r[next_v]:
                    return False
                else:
                    return True

def check_won(grid):
    # grid = grid
    # for r in range(len(grid)):
    #     len_r = len(r)
    #     for i in range(len_r[r]):
    #         if r[i] >= 32:
    #             return True
    #         else:
    #             return False
    check = [(ix, iy) for ix, row in enumerate(grid) for iy, i in enumerate(row) if i >= 32]

    if check:
        return True
    else:
        return False
def copy_grid(grid):
    grid_copy = copy.deepcopy(grid)
    return grid_copy

def grid_equal(grid1, grid2):
    if grid1 == grid2:
        return True
    else:
        return False