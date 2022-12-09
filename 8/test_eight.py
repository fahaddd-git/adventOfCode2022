import pytest
from unittest.mock import patch, mock_open
from eight import part_one, part_two

MODULE_NAME = "eight"


@pytest.fixture(scope="module")
def input():
    return """30373
25512
65332
33549
35390"""


def test_part_one_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_one() == 21


def test_part_one():
    assert part_one() == 1715


def test_part_two_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_two() == 8


def test_part_two():
    assert part_two() == 374400
