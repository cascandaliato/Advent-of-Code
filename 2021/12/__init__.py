from collections import Counter, defaultdict

from pyutils import *


def parse(lines):
    vertices = defaultdict(set)
    for line in lines:
        start, end = line.split('-')
        vertices[start].add(end)
        vertices[end].add(start)
    return vertices


def count_paths(vertices, current, visited, get_visited_copy, is_lower_node_valid):
    count = 0
    for node in vertices[current]:
        if node == 'start' or (node.islower() and not is_lower_node_valid(node, visited)):
            continue
        count += 1 if node == 'end' else count_paths(vertices, node, get_visited_copy(node,
                                                                                      visited), get_visited_copy, is_lower_node_valid)
    return count


@expect({'test1': 10, 'test2': 19, 'test3': 226})
def solve1(vertices):
    def get_visited_copy(node, visited):
        return visited.copy().union({node} if node != 'start' and node.islower() else {})

    def is_lower_node_valid(node, visited):
        return node not in visited

    return count_paths(vertices, 'start', set(), get_visited_copy, is_lower_node_valid)


@expect({'test1': 36, 'test2': 103, 'test3': 3509})
def solve2(vertices):
    def get_visited_copy(node, visited):
        visited_copy = visited.copy()
        if node.islower():
            visited_copy.update([node])
        return visited_copy

    def is_lower_node_valid(node, visited):
        return visited[node] == 0 or (visited[node] == 1 and visited.most_common(1)[0][1] < 2)

    return count_paths(vertices, 'start', Counter(), get_visited_copy, is_lower_node_valid)
