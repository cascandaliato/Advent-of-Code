from pyutils import *


def parse(commands):
    return commands


def get_sizes(commands):
    path, folders = [], {}

    commands = list(reversed(commands))
    while commands:
        tokens = commands.pop().split()
        if tokens[0] == "$":
            if tokens[1] == "cd":
                match tokens[2]:
                    case "/":
                        path = ["/"]
                    case "..":
                        path.pop()
                    case folder:
                        path.append(folder)
            if tuple(path) not in folders:
                folders[tuple(path)] = [0, []]
        else:
            folder = tuple(path)
            if tokens[0] == "dir":
                folders[folder][1].append(tuple(path + [tokens[1]]))
            else:
                folders[folder][0] += int(tokens[0])

    sizes = {}
    for folder, info in sorted(
        folders.items(), key=lambda item: len(item[0]), reverse=True
    ):
        files_size, subfolders = info
        sizes[folder] = files_size
        for subfolder in subfolders:
            sizes[folder] += sizes[subfolder]
    return sizes


@expect({'test': 95437})
def solve1(commands):
    return sum(s for s in get_sizes(commands).values() if s <= 100_000)


@expect({'test': 24933642})
def solve2(commands):
    total, minimum, sizes = 70_000_000, 30_000_000, get_sizes(commands)
    need_at_least = max(0, minimum - (total - sizes[("/",)]))
    return min(filter(lambda s: s >= need_at_least, sizes.values()))
