from pathlib import Path
from utilities import timer


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"

"""
overlapping assignments pairs inclusive []
find completely overlapping
account for which interval starts earlier
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
            if elf_1.start <= elf_2.start and elf_2.end <= elf_1.end:
                num_contained_intervals += 1
            elif elf_2.start <= elf_1.start and elf_1.end <= elf_2.end:
                num_contained_intervals += 1
    return num_contained_intervals


"""
Any overlap at all
.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7   a.start<=b.start<=a.end
......789  7-9

..34567..  3-7   b.start<=a.start<=b.end
.2345678.  2-8

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8

  2---5         
  2----6  
"""


@timer
def part_two():
    num_overlapping_intervals = 0
    with open(INPUT_FILE, "r") as inputfile:
        for line in inputfile.readlines():
            item = line.rstrip("\n").split(",")
            elf_1, elf_2 = Interval(*map(int, item[0].split("-"))), Interval(*map(int, item[1].split("-")))
            if elf_1.start <= elf_2.start <= elf_1.end:
                num_overlapping_intervals += 1
            elif elf_2.start <= elf_1.start <= elf_2.end:
                num_overlapping_intervals += 1
    return num_overlapping_intervals


if __name__ == "__main__":
    print(part_one())
    print(part_two())
