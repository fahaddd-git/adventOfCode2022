from pathlib import Path
from utilities import timer

INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"
"""
pairs of packets separated by blank line
how many pairs in right order

if both integers:
    lower integer first
if one or other list:
    convert nonlist to list
if both lists:
    left must be shorter

recursion problem. Don't know how many times we will do these operations
"""

from itertools import pairwise
from ast import literal_eval


@timer
def part_one():
    with open(INPUT_FILE, "r") as inputfile:
        valid_pair_ids = []
        counter = 1
        for left, right in pairwise(item.rstrip("\n") for item in inputfile.readlines()):
            if right == "" or left == "":
                continue
            is_valid = evaluate_packets(literal_eval(left), literal_eval(right))
            if is_valid == 1:
                valid_pair_ids.append(counter)
            counter += 1
        return sum(valid_pair_ids)


def evaluate_packets(left, right):
    match left, right:
        case int(), int():  # both ints
            if left > right:  # invalid
                return False
            if right > left:  # valid
                return True
            # returning None means we need more info and continue checking

        case int(), list():
            return evaluate_packets([left], right)
        case list(), int():
            return evaluate_packets(left, [right])
        case list(), list():  # loop thru each item in lists applying function

            for result in map(evaluate_packets, left, right):  # stops when shortest iterable exhausted
                if isinstance(result, bool):
                    return result
                # if return value is None we keep going checking values

            # need more information regarding lengths
            # outside of loop since we should check this condition last if both are lists
            if len(left) > len(right):  # invalid
                return False
            if len(right) > len(left):  # valid
                return True
            # return None  # the case of same lengths.


# from functools import cmp_to_key # alternative implementation idea


@timer
def part_two():
    with open(INPUT_FILE, "r") as inputfile:
        packets = [literal_eval(x) for x in inputfile.read().split()]
        first_key, second_key = [[[2]], [[6]]]
        first = 1 + sum(1 for x in packets if evaluate_packets(x, first_key) is True)
        second = 2 + sum(1 for x in packets if evaluate_packets(x, second_key) is True)
        return first * second
        # ordered = sorted(packets+key_packets, key=cmp_to_key(evaluate_packets), reverse=True)
        # return (1+ ordered.index(key_packets[0]) )* (1+ordered.index(key_packets[1]))


if __name__ == "__main__":
    print(part_one())
    print(part_two())
