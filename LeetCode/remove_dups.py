def remove_dups(nums):
    ii = 0
    jj = 0
    while True:
        while nums[ii] == nums[jj]:
            jj += 1
            if jj >= len(nums):
                return nums[:ii+1]
        ii += 1
        nums[ii] = nums[jj]


l = [0,0,2,2,3,3,5,5,5,5,9,9,9,10,10,22]

print(remove_dups(l))