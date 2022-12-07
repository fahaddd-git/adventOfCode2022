from pathlib import Path
from utilities import timer
from dataclasses import dataclass, field

INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"
"""
/ root dir
$ means executed command
--cd results--
123 abc   file abc size 123
dir xyz   dir called xyz exists in curr dir

determine total size of each dir= sum of file sizes
Find all directories with size total of at most 100000 (<= 100000)
Then find sum of all these directories
Files can be counted more than once
"""


@dataclass(eq=False, frozen=True)
class DirNode:
    name: str
    parent: None
    dirnode_children: dict = field(default_factory=dict)
    filenode_children: set = field(default_factory=set)


@dataclass(frozen=True)
class FileNode:
    name: str
    size: int


"""
knowing files and folders is bounded by ls or cd (something that starts with $)
"""


def construct_filetree():
    with open(INPUT_FILE, "r") as inputfile:
        curr_dirnode = DirNode("/", None)
        root = curr_dirnode
        for line in inputfile.readlines():
            command = line.rstrip("\n").split(" ")
            # ls command
            if command[1] == "ls":
                continue
            # cd command. Process found dirs and files
            if command[1] == "cd":
                # up one level
                if command[2] == "..":
                    curr_dirnode = curr_dirnode.parent
                # follow to whatever dir
                else:
                    curr_dirnode = curr_dirnode.dirnode_children.get(command[2], curr_dirnode)
            # process dirs
            elif command[0] == "dir":
                dnode = DirNode(command[1], curr_dirnode)
                curr_dirnode.dirnode_children[dnode.name] = dnode
            # process files
            else:
                fnode = FileNode(command[1], int(command[0]))
                curr_dirnode.filenode_children.add(fnode)

    return root


"""
get to where no dirnode_children
find total of files
add dirname to dict : filesize total

dir can have 1 parent
"""


def calculate_dir_sizes():
    stack = [construct_filetree()]
    visited = dict()
    while stack:
        # [dirnode(a), dirnode(d)]
        node = stack.pop()
        if node not in visited:
            # get sum
            fnode_sums = sum([f.size for f in node.filenode_children])
            visited[node] = fnode_sums
            parent_node = node.parent
            # traverse up tree updating pointers
            while parent_node:
                visited[parent_node] += fnode_sums
                parent_node = parent_node.parent
        for item in node.dirnode_children.values():
            if item not in visited:
                stack.append(item)

    return visited.values()


from itertools import filterfalse


@timer
def part_one():
    LARGEST_DIR_SIZE = 100000
    return sum(filterfalse(lambda x: x > LARGEST_DIR_SIZE, calculate_dir_sizes()))


"""
total disk space = 70000000
needed unused space = 30000000

total disk space - homedir size = curr avail size

find closest dir size to (needed unused space - curr avail size)
"""


@timer
def part_two():
    TOTAL_DISK_SPACE = 70000000
    NEEDED_UNUSED_SPACE = 30000000
    dir_sizes = calculate_dir_sizes()
    min_space = max(dir_sizes) - (TOTAL_DISK_SPACE - NEEDED_UNUSED_SPACE)
    return min(filterfalse(lambda x: x <= min_space, dir_sizes))


if __name__ == "__main__":
    print(part_one())
    print(part_two())
