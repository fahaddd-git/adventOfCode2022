import pytest
from unittest.mock import patch, mock_open
from seven import part_one, part_two

MODULE_NAME = "seven"


@pytest.fixture(scope="module")
def input():
    return """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def test_part_one_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_one() == 95437


def test_part_one():
    assert part_one() == 2104783


def test_part_two_examples(input):
    with patch(f"{MODULE_NAME}.open", mock_open(read_data=input)):
        assert part_two() == 24933642


def test_part_two():
    assert part_two() == 5883165
