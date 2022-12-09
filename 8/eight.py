from pathlib import Path
from utilities import timer


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"

"""
count number of trees visible from outside the grid when looking directly around row or column

number is height
visible if other trees shorter than      in at least one direction
edge trees always visible

0 height edge trees are visible

find amount of visible trees
ex: 21 visible  16 edge + 5 interior
    30373
    65599

37  30373 37
25  25512 25
6   65332 256
359 33549 9
359 35390 09
    
    333 0
    65599

if 9 found, no other visible

ascending order count

top_seen = 5 +2+1+1+1       new_row[i] > tallests [i]   correct
left_seen = 2+2+1+3+3      new_row[x] < new_row[y] always +1    correct 
right_seen = 2+2+4+1+2    reversed() new_row[i+1] > new_row[i]. always +1
bottom_seen = 5+2+1+1+1     new_row[i] > tallests[i] 

tallests  = [6,5,5,7,9]   shortests = [3,0,3,7,3]
new_row   = [3,5,3,9,0]

10
11
11

30373  5
25512  2

65599  1
35390  1 1
"""

"""
visible if other trees shorter than      in at least one direction
edge trees always visible

"""
from collections import namedtuple

Coordinates = namedtuple("Coordinates", ["row", "col"])


def check_ascending(input):
    """
    a list is ascending if each previous digit < curr
    """
    return all(input[x] < input[-1] for x in range(len(input) - 1))


def check_directions(grid, coords: Coordinates):  # (x,y) (row, col)
    def check_l_r():
        left = grid[coords.row][: coords.col + 1]
        right = grid[coords.row][: coords.col - 1 : -1]
        return check_ascending(left) or check_ascending(right)

    def check_t_b():
        top = [grid[x][coords.col] for x in range(coords.row + 1)]
        bottom = [grid[y][coords.col] for y in range(len(grid) - 1, coords.row - 1, -1)]
        return check_ascending(top) or check_ascending(bottom)

    return check_l_r() or check_t_b()


@timer
def part_one():
    with open(INPUT_FILE, "r") as inputfile:
        grid = [[int(letter) for letter in word] for word in inputfile.read().splitlines()]
        visible = len(grid[0]) * 2 + (len(grid) * 2 - 4)  # outer part
        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                if check_directions(grid, Coordinates(row, col)):
                    visible += 1
        return visible


"""
find highest scenic score
find how far can see to next tree or edge
"""


def calc_score(input):
    """
    a list is ascending if each previous digit < curr
    """
    if len(input) <= 1:
        return 0
    total = 1
    if input[-2] >= input[-1]:
        return 1
    for x in reversed(range(len(input) - 1)):
        if input[x] < input[-1]:
            total += 1
        else:
            return total
    return total - 1


def find_total_score(grid, coords: Coordinates):  # (x,y) (row, col)
    def calc_l_r():
        left = grid[coords.row][: coords.col + 1]
        right = grid[coords.row][: coords.col - 1 : -1]
        return calc_score(left) * calc_score(right)

    def calc_t_b():
        top = [grid[x][coords.col] for x in range(coords.row + 1)]
        bottom = [grid[y][coords.col] for y in range(len(grid) - 1, coords.row - 1, -1)]
        return calc_score(top) * calc_score(bottom)

    return calc_l_r() * calc_t_b()


@timer
def part_two():
    with open(INPUT_FILE, "r") as inputfile:
        grid = [[int(letter) for letter in word] for word in inputfile.read().splitlines()]
        # pprint(grid)
        max_score = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_score = max(max_score, find_total_score(grid, Coordinates(row, col)))
        return max_score


if __name__ == "__main__":
    print(part_one())
    print(part_two())
