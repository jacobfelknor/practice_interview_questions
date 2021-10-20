from typing import List


def findTheWinnerHelper(friends: List[int], k: int, index: int) -> int:
    # base case:
    if len(friends) == 1:
        return friends.pop()
    
    # remove index specified
    friends.pop(index)
    # calculate the new index. Should be where you currently are, 
    # plus k - 1, then modulo for circular behavior
    new_index = (index + k - 1) % len(friends)
    return findTheWinnerHelper(friends, k, new_index)
    

def findTheWinner(n: int, k: int) -> int:
    # build the friends first
    friends = list(range(1, n + 1))
    # pass to our recursive function
    return findTheWinnerHelper(friends, k, k - 1)

# should be 3
assert findTheWinner(5, 2) == 3

# should be 1
assert findTheWinner(6,5) == 1

# should be 5
assert findTheWinner(10, 4) == 5