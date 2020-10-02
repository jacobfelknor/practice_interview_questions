# Cracking the Coding Interview
# Problem 1.5
# given two strings, write a function to check if they are one edit (or zero) away


def check_replacement(str1, str2):
    diff_found = False
    for ii in range(len(str1)):
        if str1[ii] != str2[ii]:
            if diff_found:
                return False
            diff_found = True
    return True


def check_insert(short, long):
    ishort = 0
    ilong = 0
    while ishort < len(short) and ilong < len(long):
        if short[ishort] != long[ilong]:
            ilong += 1
            if ilong - ishort > 1:
                return False
        else:
            ilong += 1
            ishort += 1
    return True


def one_away(str1, str2):
    if len(str1) == len(str2):
        return check_replacement(str1, str2)
    elif len(str1) + 1 == len(str2):
        return check_insert(str1, str2)
    elif len(str1) == len(str2) + 1:
        return check_insert(str2, str1)
    return False


tests_true = [
    ("hello", "hell"),
    ("jacob", "jcob"),
    ("same", "same"),
]
tests_false = [
    ("jacob", "jaxeb"),
    ("hello", "heiio"),
    ("yes", "absolutely"),
    ("jacob", "justin"),
]

for test in tests_true:
    assert one_away(test[0], test[1]) is True

for test in tests_false:
    assert one_away(test[0], test[1]) is False
