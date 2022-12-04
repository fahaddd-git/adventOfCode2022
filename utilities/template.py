from pathlib import Path
from utilities import timer


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"


@timer
def part_one():
    with open(INPUT_FILE, "r") as inputfile:
        for line in inputfile.readlines():
            item = line.rstrip("\n")
            ...


@timer
def part_two():
    with open(INPUT_FILE, "r") as inputfile:
        for line in inputfile.readlines():
            item = line.rstrip("\n")
            ...


if __name__ == "__main__":
    print(part_one())
    print(part_two())
