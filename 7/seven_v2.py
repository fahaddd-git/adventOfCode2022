from pathlib import Path
from utilities import timer


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"

from collections import defaultdict


def parse_input():
    with open(INPUT_FILE, "r") as inputfile:
        dirs, dirstack = defaultdict(int), []
        for cmd in (x.rstrip("\n").split() for x in inputfile.readlines()):
            match cmd:
                case ("$", "cd", ".."):
                    dirstack.pop()
                case ("$", "cd", dir):
                    dirstack.append(dir)
                case ("$", "ls") | ("dir", _):
                    continue
                case (size, _):
                    size = int(size)
                    for x in (tuple(dirstack[: i + 1]) for i in range(len(dirstack))):
                        dirs[x] += size

    return dirs


@timer
def part_one():
    dirs = parse_input()
    return sum(filter(lambda v: v <= 100000, dirs.values()))


@timer
def part_two():
    TOTAL_DISK_SPACE = 70000000
    NEEDED_UNUSED_SPACE = 30000000
    dir_values = parse_input().values()
    min_space = max(dir_values) - (TOTAL_DISK_SPACE - NEEDED_UNUSED_SPACE)
    return min(filter(lambda x: x > min_space, dir_values))


if __name__ == "__main__":
    print(part_one())
    print(part_two())
