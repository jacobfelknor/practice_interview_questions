"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

"""

import random
from typing import List


# RECURSIVE
# def _minCostHelper(cost: List[int]) -> int:
#     if len(cost) == 0:
#         return 0
#     if len(cost) <= 2:
#         return cost[0]

#     return min(
#         cost[0] + _minCostHelper(cost[1:]),
#         cost[0] + _minCostHelper(cost[2:]),
#     )


# def minCostClimbingStairs(cost: List[int]) -> int:
#     # can either start from index 0 or index 1
#     return min(_minCostHelper(cost), _minCostHelper(cost[1:]))


# DP Memo
# class MinCostStair:
#     def __init__(self) -> None:
#         self.table = {}

#     def get_value(self, cost: List[int], n: int):
#         if n in self.table:
#             return self.table.get(n)
#         else:
#             val = self._minCostHelper(cost, n)
#             self.table[n] = val
#             return val

#     def _minCostHelper(self, cost: List[int], n: int) -> int:
#         if len(cost) == 0:
#             return 0
#         if len(cost) <= 2:
#             return cost[0]

#         return min(
#             cost[0] + self.get_value(cost[1:], n + 1),
#             cost[0] + self.get_value(cost[2:], n + 2),
#         )


# def minCostClimbingStairs(cost: List[int]) -> int:
#     # can either start from index 0 or index 1
#     min_cost_dp = MinCostStair()
#     _minCostHelper = min_cost_dp._minCostHelper
#     return min(_minCostHelper(cost, n=0), _minCostHelper(cost[1:], n=1))


# DP table
def minCostClimbingStairs(cost: List[int]) -> int:
    table = [None] * (len(cost) + 1)
    table[0] = cost[0]
    table[1] = cost[1]
    cost.append(0)

    for ii in range(2, len(cost)):
        table[ii] = cost[ii] + min(table[ii - 1], table[ii - 2])

    return table[-1]


cost = [10, 15, 20]

print(minCostClimbingStairs(cost))

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

print(minCostClimbingStairs(cost))

random.seed(42)
cost = random.sample(range(1, 1000), 200)

print(minCostClimbingStairs(cost))
