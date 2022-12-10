import pytest
from unittest.mock import patch, mock_open
from nine import part_one, part_two

MODULE_NAME = "nine"


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""",
            13,
        )
    ],
)
def test_part_one_examples(input, expected):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_one() == expected


def test_part_one():
    assert part_one() == 5878


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""",
            36,
        )
    ],
)
def test_part_two_examples(input, expected):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_two() == expected


def test_part_two():
    assert part_two() == 2405
