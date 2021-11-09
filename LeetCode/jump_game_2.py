"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.


Input: nums = [2,3,0,1,4]
Output: 2
"""


from typing import List
import sys


def jump_recursive(nums: List[int], hops: int = 1) -> int:
    if len(nums) <= 1:
        return hops
    else:
        hop_distance = nums[0]
        if hop_distance + 1 >= len(nums):
            return hops
        if hop_distance == 0:
            # I'm stuck here, return maxsize so that I never choose this path
            return sys.maxsize
        return min([jump_recursive(nums[next_start:], hops + 1) for next_start in range(1, hop_distance + 1)])


class JumpGame2:
    def __init__(self) -> None:
        self.table = {}

    def get_min_jumps(self, nums: List[int], hops: int = 1, n: int = 0) -> int:
        if n in self.table:
            return self.table.get(n)
        else:
            val = self.jump(nums, hops, n)
            self.table[n] = val
            return val

    def jump(self, nums: List[int], hops: int = 0, n: int = 0) -> int:
        if len(nums) <= 1:
            return hops
        else:
            hop_distance = nums[0]
            if hop_distance >= len(nums) - 1:
                return hops + 1
            if hop_distance == 0:
                # I'm stuck here, return maxsize so that I never choose this path
                return sys.maxsize
            return min(
                [
                    self.get_min_jumps(nums[next_start:], hops + 1, n + next_start)
                    for next_start in range(1, hop_distance + 1)
                ]
            )


def jump(nums: List[int]) -> int:
    jg = JumpGame2()
    return jg.jump(nums)


nums = [2, 3, 1, 1, 4]
print(jump(nums))

nums = [2, 3, 0, 1, 4]
print(jump(nums))

# not working for this case....
nums = [1, 2, 1, 1, 1]
print(jump(nums))
