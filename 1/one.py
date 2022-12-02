from pathlib import Path
import heapq


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"

def part1():
    with open(INPUT_FILE, "r") as inputfile:
        maximum=0
        elf_total = 0
        for line in inputfile.readlines():
            curr_elf_item = line.rstrip("\n")
            if curr_elf_item == "":
                maximum=max(maximum, elf_total)
                elf_total = 0
            else:
                elf_total+= int(curr_elf_item)

        return maximum

# top 3, use minheap.  Popping gives min so we want heap size 3
def part2():
    with open(INPUT_FILE, "r") as inputfile:
        q = []
        elf_total = 0
        for line in inputfile.readlines():
            curr_elf_item = line.rstrip("\n")
            if curr_elf_item == "":
                if len(q) == 3:
                    heapq.heappushpop(q, elf_total)
                else:
                    heapq.heappush(q, elf_total)
                elf_total = 0
            else:
                elf_total+= int(curr_elf_item)

        return sum(q)

if __name__=="__main__":
    print(part1())
    print(part2())