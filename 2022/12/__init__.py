from collections import deque

from pyutils import *


def parse(lines):
    grid = list(map(list, lines))
    for row, _ in enumerate(grid):
        for col, _ in enumerate(grid[0]):
            if grid[row][col] == "S":
                start = (row, col)
                grid[row][col] = "a"
            if grid[row][col] == "E":
                end = (row, col)
                grid[row][col] = "z"
    return (grid, start, end)


directions = [(+1, 0), (-1, 0), (0, +1), (0, -1)]


def bfs(grid, start, is_end, can_move):
    queue, visited = deque([(start, 0)]), set()
    while True:
        coords, depth = queue.pop()
        if coords in visited:
            continue
        visited.add(coords)
        if is_end(*coords):
            return depth
        for drow, dcol in directions:
            row, col = coords
            if 0 <= row+drow < len(grid) and 0 <= col+dcol < len(grid[0]) and can_move(grid[row][col], grid[row+drow][col+dcol]):
                queue.appendleft(((row+drow, col+dcol), depth+1))


@expect({'test': 31})
def solve1(input):
    grid, start, end = input
    return bfs(grid, start,
               is_end=lambda row, col: (row, col) == end,
               can_move=lambda frm, to: ord(to) <= ord(frm)+1)


@expect({'test': 29})
def solve2(input):
    grid, _, end = input
    return bfs(grid, end,
               is_end=lambda row, col: grid[row][col] == 'a',
               can_move=lambda frm, to: ord(to) >= ord(frm)-1)
