from collections import defaultdict
from typing import List

def longest_arith_seq(nums: List[int]) -> int:
    seqs = defaultdict(int)

    for ii in range(1, len(nums)):
        for jj in range(ii):
            diff = nums[ii] - nums[jj]
            seqCount = 1 + seqs[(jj, diff)]
            seqs[(ii, diff)] = seqCount
                
    return max(seqs.values()) + 1


print(longest_arith_seq([3,6,9,12]))