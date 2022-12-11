from pathlib import Path
from utilities import timer

INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"


def find_visibility_matrix(grid):
    """
    construct matrix that corresponds to visibility
    keep track of maximum in each row updating at every iteration
    if grid value > max then visible
    first row always visible
    """
    visible_matrix = [[True for row in range(len(grid))] for col in range(len(grid[0]))]
    for row in range(1, len(grid)):
        row_max = float("-inf")
        for col in range(len(grid[0])):
            visible_matrix[row][col] = grid[row][col] > row_max
            row_max = max(row_max, grid[row][col])
    return visible_matrix


@timer
def part_one():
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


def find_score_matrix(grid):
    """
    scoring algorithm

    m=[3,5,3,4,5]
    scores=[0,0,0,0,0]
    leftmost score is always 0

    [0] top of stack keeps track of idx of taller trees than curr (they block view)
    []  pop since m[1] > m[0]    5>3
    setscore 1-0 = 1   scores=[0,1,0,0,0]
    [1] add curr idx

    [1]  m[2] not taller than m[stack[-1]]. don't pop
    setscore 2-1 = 1 scores=[0,1,1,0,0]
    [1,2] add curr idx to stack

    [1,2] -> [1]   m[3] taller than matrix[stack[-1]]. pop from stack.
    [1]   m[3] not taller than matrix[stack[-1]]. don't pop.
    setscore 3-1 = 2 scores=[0,1,1,2,0]
    [1,3] add cur idx to stack

    [1,3]->[1] m[4] taller than matrix[stack[-1]]. pop from stack
    [1]  m[4] not taller than matrix[stack[-1]]. don't pop
    setscore 4-1 = 3 scores=[0,1,1,2,3]

    """

    scores = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]

    for i in range(len(grid)):
        stack = [0]
        for j in range(1, len(grid[0])):
            while stack and grid[i][j] > grid[i][stack[-1]]:
                stack.pop()
            scores[i][j] = j if not stack else j - stack[-1]
            stack.append(j)
    return scores


@timer
def part_two():
    with open(INPUT_FILE, "r") as inputfile:
        grid = [[int(letter) for letter in word] for word in inputfile.read().splitlines()]
        max_score = float("-inf")

        # look left   normal
        look_left = find_score_matrix(grid)
        # look right  reverse each row
        look_right = find_score_matrix([row[::-1] for row in grid])
        # look up     rotate left
        look_up = find_score_matrix(list(zip(*grid)))
        # look down   rotate right
        look_down = find_score_matrix(list(zip(*grid[::-1])))
        TOTAL_ROWS = len(grid)
        TOTAL_COLS = len(grid[0])

        for row in range(TOTAL_ROWS):
            for col in range(TOTAL_COLS):
                max_score = max(
                    look_left[row][col]
                    * look_right[row][TOTAL_COLS - col - 1]
                    * look_up[col][row]
                    * look_down[col][TOTAL_ROWS - row - 1],
                    max_score,
                )
        return max_score


if __name__ == "__main__":
    print(part_one())
    print(part_two())
