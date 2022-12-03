from pathlib import Path


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"
"""
1 item same per half of string
a-z  1-26
A-Z 27-52

find item that appears in both halves
find priority value of that item
get total of all 
"""


def get_priority_value(letter):
    """
    Finds priority value using unicode
    """
    if letter.islower():
        return ord(letter) - 96
    return ord(letter) - 38


def part_one():
    sum = 0
    with open(INPUT_FILE, "r") as inputfile:
        for line in inputfile.readlines():
            items = [*line.rstrip("\n")]
            half_index = int(len(items) / 2)
            half_1, half_2 = set(items[:half_index]), set(items[half_index:])
            [letter] = half_1 & half_2  # set intersection
            sum += get_priority_value(letter)

    return sum


"""
find same item carried by each group of 3
find priority value of item
get total of all groups of 3
"""
from itertools import zip_longest


def part_two():
    sum = 0
    with open(INPUT_FILE, "r") as inputfile:
        # use same iterator three times
        # successive values are gotten each time
        for three_lines_iter in zip_longest(*[inputfile] * 3):
            elf_group = [set(line.rstrip("\n")) for line in three_lines_iter]
            [letter] = elf_group[0] & elf_group[1] & elf_group[2]
            sum += get_priority_value(letter)

    return sum


if __name__ == "__main__":
    print(part_one())
    print(part_two())
