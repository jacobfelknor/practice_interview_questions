# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time
# and constant space. In other words, find the lowest positive integer that does not
# exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


def find_missing_pos_nlogn(input):
    """ This solves the problem in constant space, but O(nlogn) time due to the sort """
    input = sorted(input)
    min = 1
    for ii in input:
        if ii > 0:
            if ii == min:
                min += 1
            else:
                return min

    return min


if __name__ == "__main__":
    test = [4, -1, 2, 1]
    print(find_missing_pos_nlogn(test))
