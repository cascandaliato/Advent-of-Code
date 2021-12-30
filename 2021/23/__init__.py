from math import copysign
from heapq import heappop, heappush

from pyutils import *


def parse(lines):
    def to_n(amphipod):
        return str('ABCD'.index(amphipod))
    hallway = tuple('#..X.X.X.X..#')
    rooms = tuple((to_n(lines[2][3+2*i]), to_n(lines[3][3+2*i]))
                  for i in range(4))
    return hallway, rooms, set(str(n) for n in range(4)), [10**i for i in range(4)]


def can_reach(source, destination, state):
    (_, i), (r, j) = sorted((source, destination))
    hallway, rooms = state
    return all(rooms[r][n] == '.' or source == (r, n) for n in range(j+1)) and all(hallway[n] in '.X' or source == (-1, n)
                                                                                   for n in range(3+2*r, i, int(copysign(1, i-3-2*r))))


def get_new_state(amphipod, source, destination, state):
    (_, i), (r, j) = sorted((source, destination))
    hallway, rooms = state

    h_symbol = '.' if source[0] == -1 else amphipod
    r_symbol = amphipod if source[0] == -1 else '.'

    hallway = hallway[:i] + (h_symbol,) + hallway[i+1:]
    rooms = rooms[:r] + (rooms[r][:j] + (r_symbol,) +
                         rooms[r][j+1:],) + rooms[r+1:]
    return hallway, rooms


def energy(source, destination, energy_per_step):
    (_, i), (r, j) = sorted((source, destination))
    return (abs(i-3-2*r)+j+1) * energy_per_step


def solve(hallway, rooms, amphipods, energy_per_step):
    goal = tuple(tuple(str(i) for _ in range(len(rooms[0]))) for i in range(4))

    q, seen = [(0, (hallway, rooms))], set()
    while q:
        total_energy, state = heappop(q)
        hallway, rooms = state

        if state[1] == goal:
            return total_energy
        if state in seen:
            continue
        seen.add(state)

        # hallway to room
        for i, amphipod in enumerate(hallway):
            if amphipod in amphipods:
                source = (-1, i)
                for j in reversed(range(len(rooms[0]))):
                    destination = (int(amphipod), j)
                    if all(rooms[int(amphipod)][k] == amphipod for k in range(j+1, len(rooms[0]))) and can_reach(source, destination, state):
                        delta = energy(source, destination,
                                       energy_per_step[int(amphipod)])
                        heappush(
                            q, ((total_energy+delta, get_new_state(amphipod, source, destination, state))))

        # room to hallway
        for r in range(4):
            for j in range(len(rooms[0])):
                if rooms[r][j] in amphipods and any(rooms[r][k] in amphipods and rooms[r][k] != str(r) for k in range(j, len(rooms[0]))):
                    source = (r, j)
                    for i, cell in enumerate(hallway):
                        destination = (-1, i)
                        if cell == '.' and can_reach(source, destination, state):
                            delta = energy(source, destination,
                                           energy_per_step[int(rooms[r][j])])
                            heappush(q, (
                                (total_energy+delta, get_new_state(rooms[r][j], source, destination, state))))


@expect({'test': 12521})
def solve1(input):
    return solve(*input)


@expect({'test': 44169})
def solve2(input):
    hallway, rooms, amphipods, energy_per_step = input
    extra_rooms = (('3', '3'), ('2', '1'), ('1', '0'), ('0', '2'))
    rooms = tuple(room[:1] + extra_rooms[i] + room[1:]
                  for i, room in enumerate(rooms))
    return solve(hallway, rooms, amphipods, energy_per_step)
