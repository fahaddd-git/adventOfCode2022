from pathlib import Path
from utilities import timer


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"
"""
Clock ticks at constant rate called cycle
CPU has register X which starts at 1
instructions:
addx V takes 2 cycles.  After 2 cycles X increased by V
noop takes 1 cycle


noop    X=1, cycle=1
addx 3  X=1, cycle=2
        X=1, cycle=3 end cycle3 = beg cycle 4
addx -5 X-4, cycle=4


signal strength = cycle num * value of x register   during 20th, and then every 40th cycle
"""


@timer
def part_one():
    with open(INPUT_FILE, "r") as inputfile:
        cycles = 1
        register = 1
        signal_strengths = []
        for instruction in (line.rstrip("\n").split() for line in inputfile.readlines()):
            num_cycles = 0
            value = 0
            match instruction:
                case ("noop",):
                    num_cycles = 1
                case ("addx", amount):
                    num_cycles = 2
                    value = int(amount)
            for _ in range(num_cycles):
                if cycles == 20 or (cycles - 20) % 40 == 0:
                    signal_strengths.append(register * cycles)
                cycles += 1
            register += value
        return sum(signal_strengths)


"""
3 pix wide. x reg sets middle
40 wide, 6 high- 0 indexed
1 pixel drawn each cycle 

register tells middle of sprite
"""
from dataclasses import dataclass
from textwrap import wrap


@dataclass
class Coords:
    x = 0
    y = 0


@timer
def part_two():
    with open(INPUT_FILE, "r") as inputfile:
        cycles = 0
        register = 1
        pos = Coords()  # row, col
        crt = [["." for _ in range(40)] for _ in range(6)]
        for instruction in (line.rstrip("\n").split() for line in inputfile.readlines()):
            num_cycles = 0
            value = 0
            match instruction:
                case ("noop",):
                    num_cycles = 1
                case ("addx", amount):
                    num_cycles = 2
                    value = int(amount)
            for _ in range(num_cycles):
                cycles += 1
                if pos.x in [register - 1, register, register + 1]:
                    crt[pos.y][pos.x] = "#"
                pos.x += 1
                if cycles % 40 == 0:
                    pos.y += 1
                    pos.x = 0
            register += value
        res = "".join(["".join(row) for row in crt])
        return "\n".join(wrap(res, width=40))


if __name__ == "__main__":
    print(part_one())
    print(part_two())
