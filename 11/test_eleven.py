import pytest
from unittest.mock import patch, mock_open
from eleven import parse_monkeys, part_two

MODULE_NAME = "eleven"

# @pytest.fixture(scope="module")
# def input():
#     return """..."""


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""",
            10605,
        )
    ],
)
def test_part_one_examples(input, expected):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert parse_monkeys() == expected


def test_part_one():
    assert parse_monkeys() == ...


@pytest.mark.parametrize(
    ("input", "expected"),
    [("abcd", 26)],
)
def test_part_two_examples(input, expected):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_two() == expected


def test_part_two():
    assert part_two() == ...
