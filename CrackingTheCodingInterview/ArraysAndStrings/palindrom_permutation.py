# Cracking the Coding Interview
# Problem 1.4
# check if a string is a permutation of a palindrome
from functools import reduce


def is_palindrome_permutation(string):
    # based on given example, I will not consider spaces
    # "Tact Coa" --> "taco cat", "atco cta", etc.
    string = string.replace(" ", "")
    string = string.lower()
    vector = [False] * 256  # assuming ASCII
    # iterate through string. Flip bit at index ord(char).
    # for this to be a permutation of a palidrome, there must be 1 or 0 bits left as False
    for char in string:
        vector[ord(char)] = not vector[ord(char)]  # flip bit

    """ get the number of True's left """
    # count = len(list(filter(lambda x: x is True, vector)))
    """OR functor method below"""
    filtered_vector = filter(lambda x: x is True, vector)
    count = reduce(lambda _sum, elem: _sum + 1, filtered_vector, 0)
    return count in [0, 1]


tests_true = ["Tact Coa", "crarcea", "HellWoro :)llo WldHeorld :)"]
tests_false = ["kasjdfksdj", "asdffdff", "Hello World :)"]

for test in tests_true:
    assert is_palindrome_permutation(test) is True

for test in tests_false:
    assert is_palindrome_permutation(test) is False
