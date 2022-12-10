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
        cycles = 0
        register = 1
        signal_strengths = []
        cycle_multipliers = {20: 20, 60: 60, 100: 100, 140: 140, 180: 180, 220: 220}
        for instruction in (line.rstrip("\n").split() for line in inputfile.readlines()):
            r = 0
            x = 0
            match instruction:
                case ("noop",):
                    r = 1
                case ("addx", amount):
                    r = 2
                    x = amount
            for _ in range(r):
                if cycles in cycle_multipliers:
                    multiplied = register * cycle_multipliers[cycles]
                    signal_strengths.append(multiplied)
                cycles += 1
            register += int(x)
        return sum(signal_strengths)


"""
3 pix wide. x reg sets middle
40 wide, 6 high- 0 indexed
1 pixel drawn each cycle 

register tells middle of sprite
"""


@timer
def part_two():
    with open(INPUT_FILE, "r") as inputfile:
        cycles = 0
        register = 1
        pos = [0, 0]  # row, col
        crt = [["." for _ in range(40)] for x in range(6)]
        for instruction in (line.rstrip("\n").split() for line in inputfile.readlines()):
            r = 0
            x = 0
            match instruction:
                case ("noop",):
                    r = 1
                case ("addx", amount):
                    r = 2
                    x = amount
            for _ in range(r):
                cycles += 1
                if pos[1] in [register - 1, register, register + 1]:
                    crt[pos[0]][pos[1]] = "#"
                pos[1] += 1
                if cycles % 40 == 0:
                    pos = [pos[0] + 1, 0]
            register += int(x)
        for row in crt:
            print(row, sep="\n")
        return crt


if __name__ == "__main__":
    print(part_one())

    print(part_two())
