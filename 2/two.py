from pathlib import Path
from utilities import timer

"""
col1        col2
opponent    player
A=Rock      X=Rock
B=Paper     Y=Paper
C=Scissors  Z=Scissors

Score = shape score + outcome score per turn

Outcome score per turn:
0 lose
3 draw
6 win

Selected shape score:
Rock = 1
Paper = 2
Scissors = 3
"""

INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"
shapes_score = {
    "A": 1,  # Rock
    "X": 1,
    "B": 2,  # Paper
    "Y": 2,
    "C": 3,  # Scissors
    "Z": 3,
}

p1_beats_p2 = {"A": "Z", "B": "X", "C": "Y"}
p2_beats_p1 = {"X": "C", "Y": "A", "Z": "B"}
p2_beats_p1_reverse_lookup = {v: k for k, v in p2_beats_p1.items()}


@timer
def part_one():
    p2_score = 0
    with open(INPUT_FILE, "r") as inputfile:
        for line in inputfile.readlines():
            p1_shape, p2_shape = line.rstrip("\n").split(" ")
            # shape score
            p2_score += shapes_score[p2_shape]
            # outcome score
            if shapes_score[p1_shape] == shapes_score[p2_shape]:
                p2_score += 3
            elif p2_beats_p1[p2_shape] == p1_shape:
                p2_score += 6
    return p2_score


@timer
def part_two():
    p2_score = 0
    with open(INPUT_FILE, "r") as inputfile:
        for line in inputfile.readlines():
            p1_shape, p2_shape = line.rstrip("\n").split(" ")
            # draw. p1's shape score +3
            if p2_shape == "Y":
                p2_score += shapes_score[p1_shape] + 3
            # win. determine p2 winning shape + 6
            elif p2_shape == "Z":
                winning = p2_beats_p1_reverse_lookup[p1_shape]
                p2_score += shapes_score[winning] + 6
            # lose. find losing shape points
            else:
                p2_losing_shape = p1_beats_p2[p1_shape]
                p2_losing_shape_score = shapes_score[p2_losing_shape]
                p2_score += p2_losing_shape_score
    return p2_score


if __name__ == "__main__":
    print(part_one())
    print(part_two())
