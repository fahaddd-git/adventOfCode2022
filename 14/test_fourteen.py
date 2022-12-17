import pytest
from unittest.mock import patch, mock_open
from fourteen import part_one, part_two

MODULE_NAME = "fourteen"


@pytest.fixture(scope="module")
def input():
    return """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


def test_part_one_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_one() == 24


def test_part_one():
    assert part_one() == 578


def test_part_two_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_two() == 93


def test_part_two():
    assert part_two() == 24377
