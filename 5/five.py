from pathlib import Path
from utilities import timer

INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"
"""
Crates taken from top
Moved one at a time
Find top crates topology string

map str index to position line 9 of input

[1, 5, 9, 13, 17, 21, 25, 29, 33]

parsed crates  
{1: ['S', 'T', 'H', 'F', 'W', 'R'],
2: ['S', 'G', 'D', 'Q', 'W'],
3: ['B', 'T', 'W'],
4: ['D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J'],
5: ['F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z'],
6: ['L', 'P', 'T', 'C', 'V', 'B', 'S', 'G'],
7: ['Z', 'B', 'R', 'T', 'W', 'G', 'P'],
8: ['N', 'G', 'M', 'T', 'C', 'J', 'R'],
9: ['L', 'G', 'B', 'W']})
"""

from collections import defaultdict
from itertools import takewhile


def parse_puzzle():
    inputfp = open(INPUT_FILE, "r")
    reversed_puzzle = reversed(list(takewhile(lambda x: x != "\n", inputfp)))
    # relationship of what index crates appear across page
    idx_to_crate_mapping = list()
    for idx, char in enumerate(next(reversed_puzzle)):
        if char != " " and char != "\n":
            idx_to_crate_mapping.append(idx)

    crates_dict = defaultdict(list)
    for crates_line in reversed_puzzle:
        found_crates = [crates_line[x] for x in idx_to_crate_mapping]
        for idx, char in enumerate(found_crates, start=1):
            if char != " ":
                crates_dict[idx].append(char)

    return inputfp, crates_dict


from re import findall


@timer
def part_one():
    inputfile, crates_dict = parse_puzzle()
    for moves in inputfile.readlines():
        amount, from_, to = [*map(int, findall("\\d+", moves))]
        crates = [crates_dict[from_].pop() for _ in range(amount)]
        crates_dict[to].extend(crates)
    inputfile.close()
    return "".join([x[-1] for x in crates_dict.values()])


@timer
def part_two():
    inputfile, crates_dict = parse_puzzle()
    for moves in inputfile.readlines():
        amount, from_, to = [*map(int, findall("\\d+", moves))]  # [15, 6, 4]
        # can now move multiple crates. Pop multiple times and reverse
        reversed_crates = reversed([crates_dict[from_].pop() for _ in range(amount)])
        crates_dict[to].extend(reversed_crates)
    inputfile.close()
    return "".join([x[-1] for x in crates_dict.values()])


if __name__ == "__main__":
    print(part_one())
    print(part_two())
