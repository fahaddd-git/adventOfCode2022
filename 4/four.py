from pathlib import Path
from utilities import timer


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"

"""
overlapping assignments pairs inclusive []
find completely overlapping
get earliest start
check if found ending-start < other one
account for same beginnings
....567..  5-7  first.start <= second.start and first.end >= second.end
......789  7-9  False

.2345678.  2-8  first.start <= second.start and first.end >= second.end
..34567..  3-7  True

...456...  4-6  first.start <= ....
.....6...  6-6  True

.23456...  2-6
...45678.  4-8  False
  
  2---5         first.start <= second.start and first.end >= second.end fail
  2----6        reorder by ending

"""
from collections import namedtuple
from operator import itemgetter

Interval = namedtuple("Interval", ["start", "end"])


@timer
def part_one():
    num_contained_intervals = 0
    with open(INPUT_FILE, "r") as inputfile:
        for line in inputfile.readlines():
            item = line.rstrip("\n").split(",")
            elf_1, elf_2 = Interval(*map(int, item[0].split("-"))), Interval(*map(int, item[1].split("-")))
            # get interval with earliest start
            # if same start order by ending
            if elf_1.start == elf_2.start:
                first, second = sorted([elf_1, elf_2], key=itemgetter(1), reverse=True)
            else:
                first, second = sorted([elf_1, elf_2])
            if (second.start <= first.end) and (first.end >= second.end):
                num_contained_intervals += 1
    return num_contained_intervals


"""
Any overlap at all
.234.....  2-4   second.start <= first.end? False
.....678.  6-8

.23......  2-3   False
...45....  4-5

....567..  5-7   True
......789  7-9

.2345678.  2-8  True
..34567..  3-7

...456...  4-6  True
.....6...  6-6

.23456...  2-6  True
...45678.  4-8

2---5     True
2----6
"""


@timer
def part_two():
    num_overlapping_intervals = 0
    with open(INPUT_FILE, "r") as inputfile:
        for line in inputfile.readlines():
            item = line.rstrip("\n").split(",")
            elf_1, elf_2 = sorted([Interval(*map(int, item[0].split("-"))), Interval(*map(int, item[1].split("-")))])
            if elf_2.start <= elf_1.end:
                num_overlapping_intervals += 1
    return num_overlapping_intervals


if __name__ == "__main__":
    print(part_one())
    print(part_two())
