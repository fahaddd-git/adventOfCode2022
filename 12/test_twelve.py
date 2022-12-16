import pytest
from unittest.mock import patch, mock_open
from twelve import part_one, part_two

MODULE_NAME = "twelve"


@pytest.fixture(scope="module")
def input():
    return """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def test_part_one_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_one() == 31


def test_part_one():
    assert part_one() == 497


def test_part_two_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_two() == 29


def test_part_two():
    assert part_two() == 492
