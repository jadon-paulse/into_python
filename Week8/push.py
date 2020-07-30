import util
import random


# Using loops to search through values of the 2D array, when the value
# is equal too the adjacent value then merge(add) the two values when the grid
# is shifted

def reverse(grid):
    a = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            row.append(grid[i][len(grid[0]) - j - 1])
        a.append(row)
    return a


def transpose(grid):
    a = []
    for i in range(0, 4):
        row = []
        for j in range(0, 4):
            row.append(grid[j][i])
        a.append(row)
    return a


def merge(grid):
    for i in range(4):
        grid[i] = merge_line(grid[i])


def merge_line(line):
    result = [0] * len(line)
    last_merged = False
    for entry_index in range(0, len(line)):
        if line[entry_index] != 0:
            for re_index in range(0, len(result)):
                if result[re_index] == 0:
                    # result[re_index] = line[entry_index]
                    result[re_index] = result[re_index] + line[entry_index]
                    last_merged = False
                    break
                elif result[re_index + 1] == 0:
                    if result[re_index] == line[entry_index] and last_merged is False:
                        # result[re_index] = result[re_index] + line[entry_index]
                        result[re_index] *= 2
                        last_merged = True
                        break
    return result


def push_up(grid):
    mat = transpose(grid)
    merge(mat)
    mat = transpose(mat)
    util.print_grid(mat)
    return mat


def push_down(grid):
    mat = transpose(grid)
    mat = reverse(mat)
    merge(mat)
    mat = reverse(mat)
    mat = transpose(mat)
    util.print_grid(mat)
    return mat


def push_left(grid):
    merge(grid)
    util.print_grid(grid)
    return grid


def push_right(grid):
    mat = reverse(grid)
    merge(mat)
    mat = reverse(mat)
    util.print_grid(mat)
    return mat
    # util.print_grid(shift_right)