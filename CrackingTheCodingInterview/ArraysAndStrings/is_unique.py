# Cracking the Coding Interview
# Problem 1.1
# string has unique characters?


def is_unique(string):
    # use hash table (dictionary) to store seen chars
    if type(string) is not str:
        raise ValueError("is_unique argument must be a string")
    table = {}
    for letter in string:
        if table.get(letter) is not None:
            return False
        table[letter] = True
    return True


def is_unique_alt(string):
    # use ASCII values as an index to a list to check for repeats
    if type(string) is not str:
        raise ValueError("is_unique argument must be a string")
    table = [None] * 256
    for letter in string:
        if table[ord(letter)] is None:
            table[ord(letter)] = True
        else:
            return False
    return True


assert is_unique("1234") is True
assert is_unique("helloworld") is False

assert is_unique_alt("1234") is True
assert is_unique_alt("helloworld") is False

