"""

Given an integer array nums, in which exactly two elements appear 
only once and all the other elements appear exactly twice. 
Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity. Original question called
for constent space, but mine is linear space as well.
"""

from typing import List


def singleNumber(nums: List[int]) -> List[int]:
    seen_twice = {}

    for num in nums:
        if num in seen_twice:
            seen_twice[num] = True
        else:
            seen_twice[num] = False

    return [x for x in seen_twice.keys() if not seen_twice[x]]
