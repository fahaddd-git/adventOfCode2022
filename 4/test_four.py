import pytest
from unittest.mock import patch, mock_open
from four import part_one, part_two

MODULE_NAME = "four"


@pytest.fixture(scope="session")
def input():
    return """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def test_part_one_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_one() == 2


def test_part_one():
    assert part_one() == 471


def test_part_two_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_two() == 4


def test_part_two():
    assert part_two() == 888
