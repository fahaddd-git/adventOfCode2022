import pytest
from unittest.mock import patch, mock_open
from ... import part_one, part_two

MODULE_NAME = ...

# @pytest.fixture(scope="module")
# def input():
#     return """..."""


@pytest.mark.parametrize(
    ("input", "expected"),
    [("abcd", 11)],
)
def test_part_one_examples(input, expected):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_one() == expected


def test_part_one():
    assert part_one() == ...


@pytest.mark.parametrize(
    ("input", "expected"),
    [("abcd", 26)],
)
def test_part_two_examples(input, expected):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_two() == expected


def test_part_two():
    assert part_two() == ...
