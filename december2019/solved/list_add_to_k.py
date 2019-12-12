# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

import random


class SumInList:
    given = []
    k = 0

    num_dict = {}

    def __init__(self, given, k):
        self.given = given
        self.k = k

    def add_to_k_brute(self):
        # I'll start with a simple for loop brute force method
        for num1 in self.given:
            for num2 in self.given:
                if num1 + num2 == self.k:
                    return True

        return False

    def add_to_k_2pass(self):
        # better time complexity, still two passes
        for num in given:
            # find complements
            self.num_dict[self.k - num] = True

        for num in given:
            if self.num_dict.get(num):
                return True

        return False


if __name__ == "__main__":

    given = random.sample(range(1, 100000), 99999)
    k = 3
    print(k)
    testcase = SumInList(given, k)
    print(testcase.add_to_k_2pass())
