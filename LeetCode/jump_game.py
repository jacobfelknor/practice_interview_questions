"""
You are given an integer array nums.
You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
Its maximum jump length is 0, which makes it impossible to reach the last index.

"""


import random
import time
from typing import List


def canJumpRecursive(nums: List[int]) -> bool:
    # Base cases
    # 1. we made it to end!
    if len(nums) <= 1:
        return True
    # 2. we made it to position where we can't jump any more :(
    if nums[0] == 0:
        return False

    # General case. We can take hops of up to and equal to nums[0] length
    if nums[0] >= len(nums):
        # special case, we can skip right to end. Return true
        return True
    return any([canJumpRecursive(nums[jump_to:]) for jump_to in range(1, nums[0] + 1)])


class CanJump:
    def __init__(self) -> None:
        self.table = {}

    def getSubProb(self, nums: List[int], n: int) -> bool:
        if n in self.table:
            return self.table.get(n)
        else:
            ans = self.canJump(nums, n)
            self.table[n] = ans
            return ans

    def canJump(self, nums: List[int], n: int = 0) -> bool:
        # Base cases
        # 1. we made it to end!
        if len(nums) <= 1:
            return True
        # 2. we made it to position where we can't jump any more :(
        if nums[0] == 0:
            return False

        # General case. We can take hops of up to and equal to nums[0] length
        if nums[0] >= len(nums):
            # special case, we can skip right to end. Return true
            return True
        return any([self.getSubProb(nums[jump_to:], n + jump_to) for jump_to in range(1, nums[0] + 1)])


def canJump(nums: List[int]) -> bool:
    dp = CanJump()
    return dp.canJump(nums)


nums = [2, 3, 1, 1, 4]

nums = [random.randint(0, 5) for _ in range(3000)]

# t0 = time.time_ns()
# ans = canJumpRecursive(nums)
# t1 = time.time_ns()

# print(f"Recursive: {ans}, took {t1-t0} nanos")

t0 = time.time_ns()
ans = canJump(nums)
t1 = time.time_ns()

print(f"DP:        {ans}, took {t1-t0} nanos")

# nums = [3, 2, 1, 0, 4]

# print(f"Recursive: {canJumpRecursive(nums)}")
# print(f"DP: {canJump(nums)}")


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        dp = [0] * size

        if len(nums) < 2:
            return True

        # base case
        dp[0] = nums[0]

        for i in range(1, size):
            # on every step check if current index is reachable
            if dp[i - 1] == 0:
                return False

            # set current dp element as a max of jump number from current index or the one computed before minus 1 step in the dp array
            dp[i] = max(dp[i - 1] - 1, nums[i])

        return True
