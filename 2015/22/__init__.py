from math import inf
from pyutils import *


def parse(lines):
    return tuple(int(line.split(": ")[1]) for line in lines)


def play(boss_hp, dmg, hard):
    best = inf
    q = [(True, 50, 500, 0, 0, 0, 0, boss_hp)]
    while q:
        player_turn, hp, mp, mp_spent, shield, poison, recharge, boss_hp = q.pop()
        if mp_spent > best or hp <= 0 or mp <= 0:
            continue

        if hard:
            if player_turn:
                hp -= 1
                if hp <= 0:
                    continue

        armor = 0
        if shield:
            armor += 7
            shield -= 1
        if poison:
            boss_hp -= 3
            poison -= 1
        if recharge:
            mp += 101
            recharge -= 1

        if boss_hp <= 0:
            best = min(best, mp_spent)
            continue

        if player_turn:
            if mp >= 53:
                q.append(
                    (
                        False,
                        hp,
                        mp - 53,
                        mp_spent + 53,
                        shield,
                        poison,
                        recharge,
                        boss_hp - 4,
                    )
                )
            if mp >= 73:
                q.append(
                    (
                        False,
                        hp + 2,
                        mp - 73,
                        mp_spent + 73,
                        shield,
                        poison,
                        recharge,
                        boss_hp - 2,
                    )
                )
            if not shield and mp >= 113:
                q.append(
                    (
                        False,
                        hp,
                        mp - 113,
                        mp_spent + 113,
                        6,
                        poison,
                        recharge,
                        boss_hp,
                    )
                )
            if not poison and mp >= 173:
                q.append(
                    (
                        False,
                        hp,
                        mp - 173,
                        mp_spent + 173,
                        shield,
                        6,
                        recharge,
                        boss_hp,
                    )
                )
            if not recharge and mp >= 229:
                q.append(
                    (
                        False,
                        hp,
                        mp - 229,
                        mp_spent + 229,
                        shield,
                        poison,
                        5,
                        boss_hp,
                    )
                )
        else:
            hp -= max(1, dmg - armor)
            q.append((True, hp, mp, mp_spent, shield, poison, recharge, boss_hp))

    return best


def solve1(data):
    boss_hp, dmg = data
    return play(boss_hp, dmg, hard=False)


def solve2(data):
    boss_hp, dmg = data
    return play(boss_hp, dmg, hard=True)
