from pathlib import Path
from utilities import timer

INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"


def find_visibility_matrix(grid):
    # visible_matrix = [[False]*len(grid)]*len(grid[0])
    visible_matrix = [[False for row in range(len(grid))] for col in range(len(grid[0]))]
    row_max = [float("-inf")] * len(grid[0])  # each index is the max for a row
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            visible_matrix[row][col] = grid[row][col] > row_max[row]
            row_max[row] = max(row_max[row], grid[row][col])
    return visible_matrix


"""
use look left operation each time
rotate matrix to accomodate

look left
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9] ]

look right
[[3, 2, 1], 
 [6, 5, 4], 
 [9, 8, 7]]

look up
[[3, 6, 9], 
 [2, 5, 8], 
 [1, 4, 7]]

look down
[[7, 4, 1], 
[8, 5, 2], 
[9, 6, 3]]
"""


@timer
def part_one():
    with open(INPUT_FILE, "r") as inputfile:
        grid = [[int(letter) for letter in word] for word in inputfile.read().splitlines()]
        visible = 0

        # look left   normal
        look_left = find_visibility_matrix(grid)
        # # look right  reverse each row
        look_right = find_visibility_matrix([row[::-1] for row in grid])
        # # look up     rotate left
        look_up = find_visibility_matrix(list(zip(*grid)))
        # # look down   rotate right
        look_down = find_visibility_matrix(list(zip(*grid[::-1])))
        TOTAL_ROWS = len(grid)
        TOTAL_COLS = len(grid[0])

        for row in range(TOTAL_ROWS):
            for col in range(TOTAL_COLS):
                if (
                    look_left[row][col]
                    or look_right[row][TOTAL_COLS - col - 1]
                    or look_up[col][row]
                    or look_down[col][TOTAL_ROWS - row - 1]
                ):
                    visible += 1
        return visible


@timer
def part_two():
    with open(INPUT_FILE, "r") as inputfile:
        for line in inputfile.readlines():
            item = line.rstrip("\n")
            ...


if __name__ == "__main__":
    print(part_one())
    print(part_two())
