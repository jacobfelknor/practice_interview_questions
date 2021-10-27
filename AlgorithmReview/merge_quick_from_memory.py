import random
# from memory, code merge from scratch

def merge(l1: list, l2: list) -> list:
    ii = 0 # index for l1
    jj = 0 # index fro l2
    merged_list = []
    while ii < len(l1) and jj < len(l2):
        if l1[ii] <= l2[jj]:
            merged_list.append(l1[ii])
            ii += 1
        else:
            merged_list.append(l2[jj])
            jj += 1

    # fill in rest of l1 or l2, depending on which one was longer
    if ii < len(l1):
        # l1 was longer...
        merged_list.extend(l1[ii:])
    else:
        # l2 was longer...
        merged_list.extend(l2[jj:])
    
    return merged_list


def merge_sort(l: list) -> list:
    # base case
    if len(l) <= 1: return l
    # first, get midpoint of the list
    mid = len(l) // 2
    # divide into halfs
    left = l[:mid]
    right = l[mid:]

    # call merge_sort on each half
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def quick_sort_readable(l: list) -> list:
    # base case
    if len(l) <= 1: return l
    # set up temp lists... O(n) memory but readable
    less = []
    equal = []
    greater = []
    # seperate via pivot
    pivot = l[0]
    for x in l:
        if x < pivot:
            less.append(x)
        elif x > pivot: 
            greater.append(x)
        else:
            equal.append(x)
    return quick_sort_readable(less) + equal + quick_sort_readable(greater)




l = random.sample(range(-10000, 10000), 500)

print(merge_sort(l))