from pathlib import Path
from utilities import timer


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"

"""
T and H must be touching
if H is 2 setps away, T must move to meet
otherwise if not touching and not in same row or col, T moves diagonally to catch up

find positions tail visited at least once (unique positions)

R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2

use set to keep track of unique places tail has been
use coord system (x,y)
keep track of curr pos's
"""

"""
.1..4.
.H..T.
......
......
if H and T on same y plane diff x plane  

if tail.x > head.x:  tail right of head
    dist=abs(tail.x-head.x)-1
    tail.x=head.x+1  

if head.x> tail.x:            tail left of head
    dist=abs(tail.x-head.x)-1
    tail.x=head.x-1


..H... 3
......
..T... 1
..2...

if H and T on diff y plane same x plane

if tail.y > head.y:             tail above head
    dist=abs(tail.y-head.y) -1
    tail.y = head.y + 1

if head.y > tail.y:             head above tail
    dist=abs(tail.y-head.y) - 1
    tail.y = head.y -1


..H... 3
......
...T.. 1
..23..
if H and T on diff y plane diff x plane

"""


from itertools import pairwise
from dataclasses import dataclass


@dataclass
class Knot:
    x: int = 0
    y: int = 0

    def move(self, direction):
        match direction:
            case "U":
                self.y += 1
            case "R":
                self.x += 1
            case "D":
                self.y -= 1
            case "L":
                self.x -= 1

    @staticmethod
    def determine_sign(x):
        if x > 0:
            return 1
        if x < 0:
            return -1
        return 0

    def drag_follower(self, follower):
        dist_x, dist_y = self.x - follower.x, self.y - follower.y
        if abs(dist_x) > 1 or abs(dist_y) > 1:
            follower.x += self.determine_sign(dist_x)
            follower.y += self.determine_sign(dist_y)
            return True
        return False


def solve(rope_length):
    with open(INPUT_FILE, "r") as inputfile:
        seen = set()
        rope = [Knot() for _ in range(rope_length)]
        tail = rope[-1]
        for direction, spaces in (x.rstrip("\n").split() for x in inputfile.readlines()):
            for _ in range(int(spaces)):
                rope[0].move(direction)
                for leader, follower in pairwise(rope):
                    if not leader.drag_follower(follower):
                        break
                seen.add((tail.x, tail.y))
        return len(seen)


@timer
def part_one():
    return solve(2)


@timer
def part_two():
    return solve(10)


if __name__ == "__main__":
    print(part_one())
    print(part_two())
