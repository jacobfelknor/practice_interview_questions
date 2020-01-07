# This problem was asked by Google.

# The edit distance between two strings refers to the minimum number
#  of character insertions, deletions, and substitutions required to
#  change one string to the other. For example, the edit distance
#  between “kitten” and “sitting” is three: substitute the “k” for
#  “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.


class EditDistance:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.distance = 0

    def calc_edit_distance(self):
        # start with subtracting lengths of strings. Add the abs
        # of distance to edit distance
        str1_length = len(self.str1)
        str2_length = len(self.str2)
        self.distance = abs(str1_length - str2_length)

        # now iterate over the shorter string and compare letters
        # increment every time the letters don't match
        if str1_length < str2_length:
            for ii in range(str1_length):
                if self.str1[ii] != self.str2[ii]:
                    self.distance += 1
        else:
            for ii in range(str2_length):
                if self.str1[ii] != self.str2[ii]:
                    self.distance += 1

        return self.distance

    def print_strs(self):
        print(f"String 1: '{self.str1}'")
        print(f"String 2: '{self.str2}'")


if __name__ == "__main__":
    testcase = EditDistance("kitten", "sitting")

    print(testcase.calc_edit_distance())
