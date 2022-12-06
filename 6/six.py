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


@timer
def part_one():
    with open(INPUT_FILE, "r") as inputfile:
        message = inputfile.readline().rstrip("\n")
        l, r = 0, 4
        message_window = message[l:r]
        counter = Counter(message_window)
        while r <= len(message):
            # 4 distinct chars
            if len(counter) == 4:
                return r
            # < 4 distinct chars
            counter.subtract(message[l])
            if counter[message[l]] == 0:
                del counter[message[l]]

            counter.update(message[r])
            r += 1
            l += 1


"""
Find start of message marker

"""


@timer
def part_two():
    with open(INPUT_FILE, "r") as inputfile:
        message = inputfile.readline().rstrip("\n")
        l, r = 0, 14
        message_window = message[l:r]
        counter = Counter(message_window)
        while r <= len(message):
            # 4 distinct chars
            if len(counter) == 14:
                return r
            # < 4 distinct chars
            counter.subtract(message[l])
            if counter[message[l]] == 0:
                del counter[message[l]]

            counter.update(message[r])
            r += 1
            l += 1


if __name__ == "__main__":
    print(part_one())
    print(part_two())
