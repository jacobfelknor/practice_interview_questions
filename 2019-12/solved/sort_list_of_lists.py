import heapq
import random


def sort_lists(lists):
    heap = []
    heapq.heapify(heap)
    """ NOTE: If the number of lists within the parent list
              is fixed, this double for loop is actually just
              O(k*n), where k is the number of lists and n
              is the number of items within the lists. If
              k is not fixed, and can vary to infinity, this
              solution actually becomes an O(n^2) :(
    """
    for x in lists:
        for y in x:
            heapq.heappush(heap, y)
    sorted_list = []
    while heap:
        sorted_list.append(heapq.heappop(heap))
    print("sorted!")


if __name__ == "__main__":
    # normal case
    lists = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
    sort_lists(lists)
    # edge cases
    lists_empty = [[], [], []]
    sort_lists(lists_empty)

    single_empty_list = []
    sort_lists(single_empty_list)

    mixed_empty = [[], [5, 2, 9, 23, 4]]
    sort_lists(mixed_empty)

    mixed_size = [[1], [1, 3, 5], [1, 10, 20, 30, 40]]
    sort_lists(mixed_size)

    single_element = [[1]]
    sort_lists(single_element)

    # stress test
    stress = [random.sample(range(1, 100000), 99999) for i in range(40)]
    sort_lists(stress)

