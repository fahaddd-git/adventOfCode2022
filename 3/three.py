from pathlib import Path
from utilities import timer


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


@timer
def part_one():
    sum = 0
    with open(INPUT_FILE, "r") as inputfile:
        for line in inputfile.readlines():
            items = [*line.rstrip("\n")]
            half_index = int(len(items) / 2)
            [letter] = set(items[:half_index]) & set(items[half_index:])
            sum += get_priority_value(letter)

    return sum


"""
find same item carried by each group of 3
find priority value of item
get total of all groups of 3
"""


@timer
def part_two():
    sum = 0
    with open(INPUT_FILE, "r") as inputfile:
        # use same iterator three times
        # successive values are gotten each time.  "grouper" pattern
        for elves_group_tuple in zip(*[inputfile] * 3):
            elf_1, elf_2, elf_3 = [set(line.rstrip("\n")) for line in elves_group_tuple]
            [letter] = elf_1 & elf_2 & elf_3
            sum += get_priority_value(letter)

    return sum


# find -mindepth 2 -type f -name "*.py" -print0 | xargs -t -0 --replace bash -xc "poetry run python {}"

if __name__ == "__main__":
    print(part_one())
    print(part_two())
