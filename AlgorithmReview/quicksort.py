from typing import List


def quicksort_readable(l: List) -> List:
    # readable, but O(n) memory quicksort
    less = []
    equal = []
    greater = []

    if len(l) <= 1: return l

    pivot = l[0]
    for x in l:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
        
    return quicksort_readable(less) + equal + quicksort_readable(greater)




# Python3 implementation of QuickSort

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(array, start, end):
	
	# Initializing pivot's index to start
	pivot_index = start
	pivot = array[pivot_index]
	
	# This loop runs till start pointer crosses
	# end pointer, and when it does we swap the
	# pivot with element on end pointer
	while start < end:
		
		# Increment the start pointer till it finds an
		# element greater than pivot
		while start < len(array) and array[start] <= pivot:
			start += 1
			
		# Decrement the end pointer till it finds an
		# element less than pivot
		while array[end] > pivot:
			end -= 1
		
		# If start and end have not crossed each other,
		# swap the numbers on start and end
		if(start < end):
			array[start], array[end] = array[end], array[start]
	
	# Swap pivot element with element on end pointer.
	# This puts pivot on its correct sorted place.
	array[end], array[pivot_index] = array[pivot_index], array[end]
	
	# Returning end pointer to divide the array into 2
	return end
	
# The main function that implements QuickSort
def quicksort(array):
    def _qs(array, start, end):     
        if (start < end):
            # p is partitioning index, array[p]
            # is at right place
            p = partition(array, start, end)

            # Sort elements before partition
            # and after partition
            _qs(array, start, p - 1)
            _qs(array, p + 1, end)

    _qs(array, 0, len(array) - 1)           

l = [12,54,6,3,2,0,11,-5,-3,96,-8,4]
l_sorted = quicksort_readable(l)
l_sorted_2 = quicksort(l)

print(l)
print(l_sorted)
print(l)