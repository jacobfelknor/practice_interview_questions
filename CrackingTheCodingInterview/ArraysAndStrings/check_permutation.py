# Cracking the Coding Interview
# Problem 1.2
# is one string a permutation of the other?


def is_permutation(s1, s2):
    # compare character counts using a hash table
    if len(s1) != len(s2):
        return False
    letter_count_1 = {}
    letter_count_2 = {}
    for letter in s1:
        if letter_count_1.get(letter) is None:
            letter_count_1[letter] = 1
        else:
            letter_count_1[letter] += 1

    for letter in s2:
        if letter_count_2.get(letter) is None:
            letter_count_2[letter] = 1
        else:
            letter_count_2[letter] += 1

    return letter_count_1 == letter_count_2


def is_permutation_sorted(s1, s2):
    # sort the strings and compare their character values
    if len(s1) != len(s2):
        return False
    # assuming I can use built in sort methods....
    s1 = sorted(s1)
    s2 = sorted(s2)
    for ii in range(len(s1)):
        if s1[ii] != s2[ii]:
            return False
    return True


tests_true = [
    ("racecar", "rcaearc"),
    ("123", "321"),
    ("hellomynameisjacob", "myjacobisnamehello"),
]
tests_false = [("123", "441"), ("helloworld", "goodbyeworld"), ("asdfg", "gfxsa")]

for test in tests_true:
    assert is_permutation(test[0], test[1]) is True
    assert is_permutation_sorted(test[0], test[1]) is True
for test in tests_false:
    assert is_permutation(test[0], test[1]) is False
    assert is_permutation_sorted(test[0], test[1]) is False
