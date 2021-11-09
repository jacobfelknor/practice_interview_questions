"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

>>> min_sub_array_length([2,3,1,2,4,3], 7)
2
"""


from typing import List


def min_sub_array_length(nums: List[int], nsum: int) -> int:
    start = 0
    # end = 0
    min_len = float("inf")
    cur_sum = 0

    for end in range(len(nums)):
        cur_sum += nums[end]

        while cur_sum >= nsum:
            min_len = min(min_len, end - start + 1)
            cur_sum -= nums[start]
            start += 1

    if min_len == float("inf"):
        return 0
    return min_len


print(min_sub_array_length([2, 3, 1, 2, 4, 2], 7))
