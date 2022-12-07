import pytest
from unittest.mock import patch, mock_open
from five import part_one, part_two

MODULE_NAME = "five"


@pytest.fixture(scope="module")
def input():
    return """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_part_one_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_one() == "CMZ"


def test_part_one():
    assert part_one() == "ZRLJGSCTR"


def test_part_two_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_two() == "MCD"


def test_part_two():
    assert part_two() == "PRTTGRFPB"
