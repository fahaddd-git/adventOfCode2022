from pathlib import Path
from utilities import timer


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"
"""
x,y coords
x=distance to right (col)
y=distance down (row)

sand at 500,0
one sand per turn until comes to rest
falls down to bottom or rock or sand
else diagonally down left
else diagonally down right
else comes to rest on that rock

"""
from itertools import pairwise
from operator import add
from dataclasses import dataclass, field


OFFSET = 350  # offset amount of cols
ROCK = "X"
SAND = "O"
EMPTY = "."


@dataclass
class Sand:
    location: list = field(default_factory=lambda: [0, 500 - OFFSET])  # row, col = y,x
    in_abyss = False

    def fall_recursive(self, matrix):

        old_y, old_x = self.location

        def inner_func():
            y, x = self.location

            # if y+1 < bounds_y and matrix[y + 1][x] == EMPTY:
            if matrix[y + 1][x] == EMPTY:
                self.location[0] += 1

            elif matrix[y + 1][x - 1] == EMPTY:

                self.location[0] += 1
                self.location[1] -= 1

            elif matrix[y + 1][x + 1] == EMPTY:

                self.location[0] += 1
                self.location[1] += 1

            self.fall_recursive(matrix)

        try:
            inner_func()
        except IndexError:
            self.in_abyss = True
        finally:
            matrix[old_y][old_x] = EMPTY
            matrix[self.location[0]][self.location[1]] = SAND

            return self.in_abyss


@timer
def part_one():
    with open(INPUT_FILE, "r") as inputfile:
        processed = inputfile.read().rstrip("\n").split("\n")
        rocks = [x.split(" -> ") for x in processed]
        # print(more_processed)
        min_x, max_x = float("inf"), 0
        min_y, max_y = float("inf"), 0
        for z in rocks:
            for y in range(len(z)):
                z[y] = tuple(map(int, z[y].split(",")))
                min_x, max_x = min(min_x, z[y][0]), max(max_x, z[y][0])
                min_y, max_y = min(min_y, z[y][1]), max(max_y, z[y][1])

        r_padding = 1

        matrix = [[EMPTY for col in range(max_x - OFFSET + r_padding)] for row in range(max_y + r_padding)]
        # print("matrix dims", (len(matrix), len(matrix[0])))
        for paths in rocks:
            for x, y in pairwise(paths):
                dx, dy = x[0] - y[0], x[1] - y[1]
                # draw cols
                for col_draw in range(abs(dy) + 1):
                    matrix[min(x[1], y[1]) + col_draw][x[0] - OFFSET] = ROCK
                # draw rows
                for row_draw in range(abs(dx) + 1):
                    matrix[x[1]][min(x[0], y[0]) + row_draw - OFFSET] = ROCK

        sand_count = 0

        while True:
            sand = Sand()
            if sand.fall_recursive(matrix) == False:
                sand_count += 1
                continue
            else:
                break
        return sand_count


@timer
def part_two():
    with open(INPUT_FILE, "r") as inputfile:
        processed = inputfile.read().rstrip("\n").split("\n")
        rocks = [x.split(" -> ") for x in processed]
        min_x, max_x = float("inf"), 0
        min_y, max_y = float("inf"), 0
        for z in rocks:
            for y in range(len(z)):
                z[y] = tuple(map(int, z[y].split(",")))
                min_x, max_x = min(min_x, z[y][0]), max(max_x, z[y][0])
                min_y, max_y = min(min_y, z[y][1]), max(max_y, z[y][1])

        bottom_padding = 60

        matrix = [
            [EMPTY for col in range(max_x - OFFSET + bottom_padding * 3)] for row in range(max_y + bottom_padding)
        ]
        for paths in rocks:
            for x, y in pairwise(paths):
                dx, dy = x[0] - y[0], x[1] - y[1]
                # draw cols
                for col_draw in range(abs(dy) + 1):
                    matrix[min(x[1], y[1]) + col_draw][x[0] - OFFSET] = ROCK
                # draw rows
                for row_draw in range(abs(dx) + 1):
                    matrix[x[1]][min(x[0], y[0]) + row_draw - OFFSET] = ROCK
        # draw floor
        for col in range(len(matrix[0])):
            matrix[max_y + 2][col] = ROCK

        sand_count = 0

        while True:
            sand = Sand()
            sand.fall_recursive(matrix)
            sand_count += 1
            if sand.location == [0, 500 - OFFSET]:
                break
        return sand_count


if __name__ == "__main__":
    print(part_one())
    print(part_two())
