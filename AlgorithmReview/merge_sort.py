from typing import List

def merge(l1: List, l2: List) -> List:
    merged = []
    ii = 0
    jj = 0
    while ii < len(l1) and jj < len(l2):
        if l1[ii] <= l2[jj]:
            merged.append(l1[ii])
            ii += 1
        else:
            merged.append(l2[jj])
            jj += 1
    
    # there may be some left in either half
    if ii < len(l1):
        merged.extend(l1[ii:])
    if jj < len(l2):
        merged.extend(l2[jj:])
    
    return merged


def merge_sort(l: List) -> List:
    if len(l) == 1: return l

    # midpoint of array
    mid = len(l) // 2 # integer division
    # left half
    left = l[:mid]
    # right half
    right = l[mid:]
    
    # recurse on left
    left_sorted = merge_sort(left)
    # recurse on right
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)
    



l = [4,6,3,2,6,6,7,33,7,54]
l_sorted = merge_sort(l)

print(l)
print(l_sorted)


