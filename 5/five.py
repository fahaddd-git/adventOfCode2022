from pathlib import Path
from utilities import timer
from pprint import pprint

INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"
"""
Crates taken from top
Moved one at a time
Find top crate
"""


def parse_puzzle():
    ...

"""
map crates to indices

map location to indices
{1: 1, 5: 2, 9: 3, 13: 4, 17: 5, 21: 6, 25: 7, 29: 8, 33: 9}

"""
from collections import defaultdict
import re
@timer
def part_one():
    with open(INPUT_FILE, "r") as inputfile:
        input = inputfile.read().rstrip("\n").splitlines()
        idx_to_crate_mapping=dict()
        for nums in input[8:9]:
            for x in range(len(nums)):
                if nums[x] != " " :
                    idx_to_crate_mapping[x] = int(nums[x])
            # print(idx_to_crate_mapping)
        crates_dict=defaultdict(list)
        for crates_line in reversed(input[0:8]):
            # add to idx dict
            for idx, char in enumerate(crates_line):
                # corresponding index found
                if idx in idx_to_crate_mapping:
                    # [ ] never will be in idx_to_crate_mapping
                    if char != " " :
                        crates_dict[idx_to_crate_mapping[idx]].append(char)
        """
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
        # pprint(crates_dict)
        # parse and execute moves
        for moves in input[10:]:
            moves=[*map(int, re.findall('\\d+', moves))]
            # print(moves)
            for amount in range(moves[0]):
                crate = crates_dict[moves[1]].pop()
                crates_dict[moves[2]].append(crate)
        return "".join([x[-1] for x in crates_dict.values()])


@timer
def part_two():
    with open(INPUT_FILE, "r") as inputfile:
        input = inputfile.read().rstrip("\n").splitlines()
        idx_to_crate_mapping=dict()
        for nums in input[8:9]:
            for x in range(len(nums)):
                if nums[x] != " " :
                    idx_to_crate_mapping[x] = int(nums[x])
            # print(idx_to_crate_mapping)
        crates_dict=defaultdict(list)
        for crates_line in reversed(input[0:8]):
            # add to idx dict
            for idx, char in enumerate(crates_line):
                # corresponding index found
                if idx in idx_to_crate_mapping:
                    # [ ] never will be in idx_to_crate_mapping
                    if char != " " :
                        crates_dict[idx_to_crate_mapping[idx]].append(char)
        """
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
        # pprint(crates_dict)
        # parse and execute moves
        for moves in input[10:]:
            moves=[*map(int, re.findall('\\d+', moves))]
            # can now move multiple crates
            crates = reversed([crates_dict[moves[1]].pop() for y in range(moves[0])])
            crates_dict[moves[2]].extend(crates)

        return "".join([x[-1] for x in crates_dict.values()])

if __name__ == "__main__":
    print(part_one())
    print(part_two())
