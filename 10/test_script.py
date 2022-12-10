import pytest
from unittest.mock import patch, mock_open
from ten import part_one, part_two

MODULE_NAME = "ten"


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_part_one_examples(input, expected):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_one() == expected


def test_part_one():
    assert part_one() == ...


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_part_two_examples(input, expected):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_two() == expected


def test_part_two():
    assert part_two() == ...
