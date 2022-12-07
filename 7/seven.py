from pathlib import Path
from utilities import timer

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


class DirNode:
    def __init__(self, name, parent, dirnode_children: list, filenode_children: list):
        self.name = name
        self.parent = parent
        self.dirnode_children = dirnode_children
        self.filenode_children = filenode_children

        # def __eq__(self, other):
        #     return self.name == other.name and self.parent == other.parent


class FileNode:
    def __init__(self, name, size, dir_parent: DirNode):
        self.name = name
        self.size = size
        self.dir_parent = dir_parent

    # def __eq__(self, other):
    #     return self.name == other.name and self.size == other.size and self.dir_parent == other.dir_parent


"""
knowing files and folders is bounded by ls or cd (something that starts with $)
"""


def process_input():
    with open(INPUT_FILE, "r") as inputfile:
        file_stack = []
        dir_stack = []
        curr_dirnode = DirNode("/", None, [], [])
        root = curr_dirnode
        for line in inputfile.readlines():
            command = line.rstrip("\n").split(" ")
            # ls command
            if command[0] == "$" and command[1] == "ls":
                continue
            # cd command. Process found dirs and files
            if command[0] == "$" and command[1] == "cd":
                # process files
                while file_stack:
                    file = file_stack.pop()
                    fnode = FileNode(file[1], int(file[0]), curr_dirnode)
                    if fnode not in curr_dirnode.filenode_children:
                        curr_dirnode.filenode_children.append(fnode)
                # process dirs
                while dir_stack:
                    dir = dir_stack.pop()
                    # name, parent, dirnode_children, filenode_children
                    dnode = DirNode(dir, curr_dirnode, [], [])
                    if dnode not in curr_dirnode.dirnode_children:
                        curr_dirnode.dirnode_children.append(dnode)
                # go to next place in cd
                if command[2] == "..":
                    curr_dirnode = curr_dirnode.parent
                # follow to whatever dir
                else:
                    for item in curr_dirnode.dirnode_children:
                        if item.name == command[2]:
                            curr_dirnode = item
                            break
            # [b, ...]
            elif command[0] == "dir":
                # folder name
                dir_stack.append(command[1])
            # file [123123, "b.txt"]
            else:
                file_stack.append(command)

    # copy pasta from before. TODO: make better
    while file_stack:
        file = file_stack.pop()
        fnode = FileNode(file[1], int(file[0]), curr_dirnode)
        if fnode not in curr_dirnode.filenode_children:
            curr_dirnode.filenode_children.append(fnode)
    # process dirs
    while dir_stack:
        dir = dir_stack.pop()
        # name, parent, dirnode_children, filenode_children
        dnode = DirNode(dir, curr_dirnode, [], [])
        if dnode not in curr_dirnode.dirnode_children:
            curr_dirnode.dirnode_children.append(dnode)
    return root


"""
get to where no dirnode_children
find total of files
add dirname to dict : filesize total

dir can have 1 parent
"""


def calculate_dir_sizes():
    stack = [process_input()]
    visited = dict()
    while stack:
        # [dirnode(a), dirnode(d)]
        node = stack.pop()
        if node not in visited:
            # get sum
            fnode_sums = sum([f.size for f in node.filenode_children])
            visited[node] = fnode_sums
            other_node = node
            # traverse up tree updating pointers
            while other_node.parent:
                visited[other_node.parent] += fnode_sums
                other_node = other_node.parent
        for item in node.dirnode_children:
            if item not in visited:
                stack.append(item)

    return visited


@timer
def part_one():
    return sum([x for x in calculate_dir_sizes().values() if x <= 100000])


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
    dir_sizes = calculate_dir_sizes().values()
    filtered = [x for x in dir_sizes if max(dir_sizes) - (TOTAL_DISK_SPACE - NEEDED_UNUSED_SPACE) <= x]
    return min(filtered)


if __name__ == "__main__":
    print(part_one())
    print(part_two())
