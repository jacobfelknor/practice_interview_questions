# Cracking the Coding Interview
# Problem 1.3
# URLify... i.e. replace all spaces in a string with '%20'


def replace_spaces(string):
    # this is the most obvious solution using built in python methods...
    # not sure this is how they intend for me to solve the problem though
    string = string.strip()
    return string.replace(" ", "%20")


def replace_spaces_manual(string):
    # simply iterate through string and replace manually
    string = list(string.strip())
    for ii in range(len(string)):
        if string[ii] == " ":
            string[ii] = "%20"
    return "".join(string)


tests = [
    ("Mr John Smith  ", "Mr%20John%20Smith"),
    ("two  spaces", r"two%20%20spaces"),
    ("nospaces", "nospaces"),
]
for test in tests:
    assert replace_spaces(test[0]) == test[1]
    assert replace_spaces_manual(test[0]) == test[1]
