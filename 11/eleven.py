from pathlib import Path
from utilities import timer


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"

"""
starting items = worry level for each item in order
operation = how worry level changes as item is inspected
test = how monkey uses worry level to decide what to do next

loop for each starting item
inspect starting item -> item_worry_level=operation ->  item_worry_level//3 -> do test and pass to next monkey

[31,23,2]  take from left, append to right. queue
if has no items this monkeys turn ends. go to next monkey

find 2 most active monkeys.  handled most items non distinct.  multiply together.
"""
from re import findall
from dataclasses import dataclass, field
from collections import deque


@dataclass
class Monkey:
    num: int
    operation: None = None
    test: None = None
    items: deque = field(default_factory=deque)  #  in-->[]-->out
    if_true: None = None
    if_false: None = None
    monkey_counter: int = 0


# operations = {
#     "*": lambda x, y: x * y,
# }


functs = [
    lambda x: x * 11,
    lambda x: x + 1,
    lambda x: x + 7,
    lambda x: x + 3,
    lambda x: x * x,
    lambda x: x + 4,
    lambda x: x * 5,
    lambda x: x + 8,
]

test_functions = [lambda x: x * 19, lambda x: x + 6, lambda x: x * x, lambda x: x + 3]


def parse_monkeys(num_monkeys, functions):
    with open(INPUT_FILE, "r") as inputfile:
        monkeys = [Monkey(x, functions[x]) for x in range(num_monkeys)]
        curr_monkey = 0
        for all_monkeys in zip(*[inputfile] * 7):

            monkey_input = [findall("\\d+", x.strip()) for x in all_monkeys if x.strip() != ""]
            # print(monkey_input)
            for idx, input in enumerate(monkey_input):
                match idx:
                    case 0:
                        continue
                    case 1:
                        monkeys[curr_monkey].items.extendleft(list(map(int, input)))
                    case 2:
                        continue
                    case 3:  # test
                        monkeys[curr_monkey].test = int(input[0])
                    case 4:
                        monkeys[curr_monkey].if_true = int(*input)
                    case 5:
                        monkeys[curr_monkey].if_false = int(*input)
                        # operation_line = all_monkeys[2].rstrip("\n").strip().split(" ")[-2:]
                        # if operation_line[0] == "*":

            curr_monkey += 1  #     print(operation_line)
            # print(monkey_input)
            # print("\n")
        return monkeys


@timer
def part_one():
    all_monkeys = parse_monkeys(8, functs)
    for _ in range(20):
        for monkey in all_monkeys:
            while monkey.items:
                item = monkey.items.pop()
                item = monkey.operation(item)
                item = item // 3
                is_test_successful = item % monkey.test == 0
                selected_monkey = monkey.if_true if is_test_successful else monkey.if_false
                all_monkeys[selected_monkey].items.appendleft(item)
                monkey.monkey_counter += 1

    top1, top2, *_ = sorted([m.monkey_counter for m in all_monkeys], reverse=True)
    return top1 * top2


from math import lcm


@timer
def part_two():
    all_monkeys = parse_monkeys(8, functs)
    least_common_multiple = lcm(*[x.test for x in all_monkeys])
    for _ in range(10000):
        for monkey in all_monkeys:
            while monkey.items:
                item = monkey.items.pop()
                item = item % least_common_multiple
                item = monkey.operation(item)
                remainder = item % monkey.test
                selected_monkey = monkey.if_true if remainder == 0 else monkey.if_false
                all_monkeys[selected_monkey].items.appendleft(item)
                monkey.monkey_counter += 1

    top1, top2, *_ = sorted([m.monkey_counter for m in all_monkeys], reverse=True)
    return top1 * top2


if __name__ == "__main__":
    print(part_one())
    print(part_two())
