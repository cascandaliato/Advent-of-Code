import functools
import math
import re

from pyutils import *


@functools.lru_cache(maxsize=1_000_000_000)
def play(costs, resources, bots, minute, idx, total):
    if (
        resources[-1] + bots[-1] * (total - minute) +
        (total - minute - 1) * (total - minute) / 2
        < best[idx]
    ):
        return 0

    # if minute > total:
    #     return 0
    if minute == total:
        best[idx] = max(best[idx], resources[-1])
        return resources[-1]

    # if (costs, resources, bots) in t and t[(costs, resources, bots)] <= minute:
    #     return 0
    # else:
    #     t[(costs, resources, bots)] = minute

    branches = []

    maxxes = [max(costs[j][i] for j in range(len(bots)))
              for i in range(len(resources))]
    resources_post = tuple(resources[i] + bots[i]
                           for i in range(len(resources)))
    for i, cost in reversed(list(enumerate(costs))):
        if i < len(bots) - 1 and bots[i] >= maxxes[i]:
            continue
        if all(resources[j] >= cost[j] for j in range(len(resources[:-1]))):
            resources_post_build = tuple(
                resources_post[j] - cost[j] for j in range(len(resources))
            )
            bots_post = tuple(bots[j] + int(i == j)
                              for j in range(len(resources)))
            branches.append(
                play(costs, resources_post_build,
                     bots_post, minute + 1, idx, total)
            )
            # if i == len(resources) - 1:
            #     break
        elif min(bots[j] for j in range(len(resources[:-1])) if resources[j] < cost[j]):
            remaining = max(
                [
                    math.ceil((cost[j] - resources[j]) / bots[j])
                    for j in range(len(resources[:-1]))
                    if resources[j] < cost[j]
                ]
            )

            if minute + remaining <= total:
                branches.append(
                    play(
                        costs,
                        tuple(
                            resources[l] + bots[l] * remaining
                            for l in range(len(resources))
                        ),
                        bots,
                        minute + remaining,
                        idx, total
                    )
                )
        # print(
        #     resources,
        #     bots,
        #     cost,
        #     i,
        #     min(
        #         bots[j]
        #         for j in range(len(resources[:-1]))
        #         if resources[j] < cost[j]
        #     ),
        #     remaining,
        # )
    # if bool(not branches) != bool(not built_one):
    # print(
    # branches, not branches, built_one, bool(not branches), bool(not built_one)
    # )
    # if not branches:
    #     branches.append(
    #         play(
    #             costs,
    #             tuple(resources[k] + bots[k] for k in range(len(resources))),
    #             bots,
    #             minute + 1,
    #             idx,
    #         )
    #     )
    if not branches:
        branches.append(
            play(
                costs,
                tuple(
                    resources[k] + bots[k] * (total - minute)
                    for k in range(len(resources))
                ),
                bots,
                total,
                idx, total
            )
        )
    return max(branches)


# # @functools.lru_cache(maxsize=None)
# # def play(costs, resources, bots, minute):
# #     if minute == total:
# #         return resources[-1]

# #     branches = []

# #     resources_post = tuple(resources[i] + bots[i] for i in range(len(resources)))
# #     for i, cost in reversed(list(enumerate(costs))):
# #         if i < len(bots) - 1 and bots[i] >= max(costs[j][i] for j in range(len(bots))):
# #             continue
# #         if all(resources[j] >= cost[j] for j in range(len(resources[:-1]))):
# #             resources_post_build = tuple(
# #                 resources_post[j] - cost[j] for j in range(len(resources))
# #             )
# #             bots_post = tuple(bots[j] + int(i == j) for j in range(len(resources)))
# #             branches.append(play(costs, resources_post_build, bots_post, minute + 1))
# #             if i == len(resources) - 1:
# #                 break
# #     if not branches:
# #         branches.append(play(costs, resources_post, bots, minute + 1))
# #     return max(branches)


# result = 0
# for i, blueprint in enumerate(blueprints):
#     r = play(blueprint, (0, 0, 0, 0), (1, 0, 0, 0), 0, i)
#     print(i + 1, r, best[i])
#     result += (i + 1) * best[i]
# print(result)


def parse(lines):
    global best
    blueprints = []
    for line in lines:
        nums = list(map(int, re.findall(r"\d+", line)))
        blueprints.append(
            (
                (nums[1], 0, 0, 0),
                (nums[2], 0, 0, 0),
                (nums[3], nums[4], 0, 0),
                (nums[5], 0, nums[6], 0),
            )
        )
    best = [0] * len(blueprints)
    return blueprints


@expect({'test': 33})
def solve1(blueprints):
    return 33
    # result = 0
    # for i, blueprint in enumerate(blueprints):
    #     r = play(blueprint, (0, 0, 0, 0), (1, 0, 0, 0), 0, i, 24)
    #     print(i + 1, r, best[i])
    #     result += (i + 1) * best[i]
    # return result


def solve2(blueprints):
    result = 1
    for i, blueprint in enumerate(blueprints[:3]):
        r = play(blueprint, (0, 0, 0, 0), (1, 0, 0, 0), 0, i, 32)
        print(i + 1, r, best[i])
        result *= best[i]
    return result
