from pathlib import Path
from utilities import timer


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"
"""
find first position where 4 most recently received chars different
return num chars from beginning after

count occurences in window
if counter length is 4 then answer found
if counter length < 4
    if leftmost char is 1 in counter delete from counter
    otherwise decrement
increment left and right sides of window
add these to counter
"""

from collections import Counter


def solve_puzzle(window_size):
    with open(INPUT_FILE, "r") as inputfile:
        message = inputfile.readline().rstrip("\n")
        left, right = 0, window_size
        counter = Counter(message[left:right])
        while right < len(message):
            # window_size distinct chars
            if len(counter) == window_size:
                return right
            # < window_size distinct chars
            counter[message[left]] -= 1
            if counter[message[left]] == 0:
                del counter[message[left]]

            counter[message[right]] += 1
            right += 1
            left += 1
        raise IndexError("No match found")


@timer
def part_one():
    return solve_puzzle(4)


@timer
def part_two():
    return solve_puzzle(14)


if __name__ == "__main__":
    print(part_one())
    print(part_two())
