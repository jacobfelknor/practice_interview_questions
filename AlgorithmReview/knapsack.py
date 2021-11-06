# knapsack niave recursive


import random


def knapSackRecursive(W, weights, values):
    if W == 0 or len(weights) < 1:
        return 0

    if weights[0] > W:
        # if current weight exceeds available weight
        return knapSackRecursive(W, weights[1:], values[1:])
    else:
        # return max of taking item and getting the value
        # or passing up item and moving on
        take = values[0] + knapSackRecursive(W - weights[0], weights[1:], values[1:])
        skip = knapSackRecursive(W, weights[1:], values[1:])
        return max(take, skip)


class KnapSack:
    def __init__(self) -> None:
        self.table = {}

    def get_value(self, W, weights, values, n):
        if (W, n) in self.table:
            return self.table.get((W, n))
        else:
            ans = self.solve(W, weights, values, n)
            self.table[(W, n)] = ans
            return ans

    def solve(self, W, weights, values, n=0):
        if W == 0 or len(weights) < 1:
            return 0

        if weights[0] > W:
            # if current weight exceeds available weight
            return self.get_value(W, weights[1:], values[1:], n + 1)
        else:
            # can either take it or leave it
            take = values[0] + self.get_value(
                W - weights[0], weights[1:], values[1:], n + 1
            )
            skip = self.get_value(W, weights[1:], values[1:], n + 1)
            return max(take, skip)


# Driver Code
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

print(f"Niave Recursive: {knapSackRecursive(W, weights, values)}")

knapsack = KnapSack()

print(f"Memoized: {knapsack.solve(W, weights, values)}")


values = random.sample(range(0, 1000), 200)
weights = random.sample(range(0, 1000), 200)
W = 1000

# takes forever
# print(f"Niave Recursive: {knapSackRecursive(W, weights, values)}")

knapsack = KnapSack()

print(f"Memoized: {knapsack.solve(W, weights, values)}")
