import pytest
from unittest.mock import patch, mock_open
from thirteen import part_one, part_two
from pathlib import Path

MODULE_NAME = "thirteen"
TEST_INPUT_FILE = Path(__file__).parent.resolve() / "test_input.txt"


@pytest.fixture(scope="module")
def input():
    with open(TEST_INPUT_FILE) as test_file:
        yield test_file.read()


def test_part_one_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_one() == 13


def test_part_one():
    assert part_one() == 6086


def test_part_two_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_two() == 140


def test_part_two():
    assert part_two() == 27930
