from pathlib import Path
from utilities import timer


INPUT_FILE = Path(__file__).parent.resolve() / "input.txt"

"""
elevations a-z  lowest-highest
S=start at  elevation a
end=E at elevation z

as few steps as possible
can move u,d,l,r each step
can only move 1 elevation higher, any amount lower

djikstras (greedy algo)
update estimates
choose next vertex (unexplored with smallest est)

each pos is a vertex
each path is weight 1
can only move to within 1 > height or any lower

start at end which is the height z
valid moves are up within 1, same, or down any amount
new pos- old pos >= -1
"""


def create_matrix():
    with open(INPUT_FILE, "r") as inputfile:
        input = inputfile.read().splitlines()
        return input


def get_start_end(matrix):
    start, end = (0, 0), (0, 0)
    for idx, row in enumerate(matrix):
        try:
            start = (idx, row.index("S"))
        except Exception:
            pass
        try:
            end = (idx, row.index("E"))
        except Exception:
            pass
    return start, end


import heapq
from collections import defaultdict
from string import ascii_lowercase


def create_adjacency_map(grid):
    """
    find path can go from each
    options are up,down,left,right
    """
    adj_map = defaultdict(list)
    # map chars to value
    letter_values = {char: value for value, char in enumerate(ascii_lowercase, start=1)}
    letter_values |= {"S": letter_values["a"], "E": letter_values["z"]}
    """
    ['Sabqponm', 
     'abcryxxl', 
     'accszExk', 
     'acctuvwj', 
     'abdefghi']
    """
    rows = len(grid)
    cols = len(grid[0])
    directions = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}  # possible ways to move
    for row in range(rows):
        for col in range(cols):
            curr_value = grid[row][col]
            curr_location = (row, col)
            for direction in directions.values():  # calc each possible move
                new_row, new_col = curr_location[0] + direction[0], curr_location[1] + direction[1]
                if 0 > new_row or new_row >= rows or 0 > new_col or new_col >= cols:
                    continue
                # valid move if new - old >= -1.  ex: z-t valid (26-20).  a-b valid (1-2). a-c not valid (1-3)
                # start at End aka z
                if letter_values[grid[new_row][new_col]] - letter_values[curr_value] >= -1:
                    adj_map[(curr_location)].append((new_row, new_col))
    return adj_map


def find_moves_djikstra(adj_map, start):
    """
    djikstra's algo
    each path length aka edge is 1 in this problem
    """
    heap = [(0, start)]  # (distance, (row,col))
    distances = {k: float("inf") for k in adj_map.keys()}
    distances.update({start: 0})
    while heap:
        dist, coord = heapq.heappop(heap)
        for vertex in adj_map[coord]:
            if dist + 1 < distances[vertex]:
                distances[vertex] = dist + 1
                heapq.heappush(heap, (dist + 1, vertex))
    return distances


def create_paths():
    matrix = create_matrix()
    start, end = get_start_end(matrix)
    adj_map = create_adjacency_map(matrix)
    dijkstra_result = find_moves_djikstra(adj_map, end)
    return dijkstra_result, start, end


@timer
def part_one():
    paths, start, end = create_paths()
    return paths[start]


@timer
def part_two():
    """
    get lowest cost path to E from any a path
    dijkstra's gives cost from start vertex to all other vertices
    """
    paths, *_ = create_paths()
    matrix = create_matrix()
    return min(l for (x, y), l in paths.items() if matrix[x][y] in "aS")


if __name__ == "__main__":

    print(part_one())
    print(part_two())
