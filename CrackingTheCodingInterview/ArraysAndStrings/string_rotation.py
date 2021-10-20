
def is_substring(s1: str, s2: str) -> bool:
    # check if s1 is a substring of s2
    return s1 in s2

def string_rotation_BRUTE(s1: str, s2: str) -> bool:
    # check if s2 is a rotation of s1
    # additional constraint that only one call to is_substring is allowed
    if len(s1) != len(s2):
        # can't have a rotation if the strings are of different lengths
        return False
    if s1 == s2:
        # the strings are already equal
        return True

    s1_chars = list(s1)
    
    for ii in range(len(s1)):
        # rotate s1 one char at a time, check if it's equal to s2
        s1_chars.append(s1_chars.pop(0))
        if "".join(s1_chars) == s2:
            return True
        
    return False


def string_rotation(s1: str, s2: str) -> bool:
    # check if s2 is a rotation of s1
    # additional constraint that only one call to is_substring is allowed
    if len(s1) != len(s2):
        # can't have a rotation if the strings are of different lengths
        return False
    if s1 == s2:
        # the strings are already equal
        return True

    # any rotation must also be in the string "doubled"
    test_str = s1 + s1
    return is_substring(s2, test_str)

    # second half 

# given example
s1 = "waterbottle"
s2 = "ottlewaterb"
assert string_rotation_BRUTE(s1, s2)
assert string_rotation(s1, s2)

# my own example
s1 = "interviewsarehard"
s2 = "sarehardinterview"
assert string_rotation_BRUTE(s1, s2)
assert string_rotation(s1, s2)

# my own example
s1 = "jfhjdlkggldsijd"
s2 = "lkggldsijdjfhjd"
assert string_rotation_BRUTE(s1, s2)
assert string_rotation(s1, s2)

# my own example
s1 = "jfhjglkggldsijd"
s2 = "lkggldsijdjfhjd"
assert not string_rotation_BRUTE(s1, s2)
assert not string_rotation(s1, s2)

# same string
s1 = "waterbottle"
s2 = "waterbottle"
assert string_rotation_BRUTE(s1, s2)
assert string_rotation(s1, s2)

# different lengths
s1 = "water"
s2 = "waterbottle"
assert not string_rotation_BRUTE(s1, s2)
assert not string_rotation(s1, s2)