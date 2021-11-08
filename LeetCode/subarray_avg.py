"""
Given an array of integers arr and two integers k and threshold.

Return the number of sub-arrays of size k and average greater than or equal to threshold.

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. 
All other sub-arrays of size 3 have averages less than 4 (the threshold).


Input: arr = [1,1,1,1,1], k = 1, threshold = 0
Output: 5

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5.
Note that averages are not integers.
"""


from typing import List


def numOfSubarraysBrute(arr: List[int], k: int, threshold: int) -> int:
    ii = 0
    counter = 0

    while ii < len(arr) - k + 1:
        subarray = arr[ii:ii+k]
        if sum(subarray) / k >= threshold:
            counter += 1
        ii += 1
    return counter

def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    ii = 0
    counter = 0

    curr_sum = sum(arr[ii:k])
    if curr_sum / k >= threshold:
        counter += 1
    ii += 1
    while ii < len(arr) - k + 1:
        curr_sum = curr_sum - arr[ii-1] + arr[k+ii-1]
        if curr_sum / k >= threshold:
            counter += 1
        ii += 1
    return counter



arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
# output should be 3
print(numOfSubarrays(arr, k, threshold))

arr = [1,1,1,1,1]
k = 1
threshold = 0
# output should be 5
print(numOfSubarrays(arr, k, threshold))

arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5
# output should be 6
print(numOfSubarrays(arr, k, threshold))

arr = [7,7,7,7,7,7,7]
k = 7
threshold = 7
# output should be 1
print(numOfSubarrays(arr, k, threshold))

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
# output should be 3
print(numOfSubarrays(arr, k, threshold))