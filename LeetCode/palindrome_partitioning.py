"""
Given a string s, partition s such that every substring of the partition is a palindrome.
 Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]


Input: s = "a"
Output: [["a"]]

"""


from typing import List


def is_palindrome(s: str) -> bool:
    if len(s) in [0, 1]:
        return True
    ii = 0
    jj = len(s) - 1
    while ii < jj:
        if s[ii] != s[jj]:
            return False
        ii += 1
        jj -= 1
    return True


class PalindromePartition:
    def __init__(self) -> None:
        self.table = {}

    def get_partition(self, s: str) -> List[List[str]]:
        if s in self.table:
            return self.table[s]
        else:
            ans = self.partition(s)
            self.table[s] = ans
            return ans

    def partition(self, s: str) -> List[List[str]]:
        if len(s) < 1:
            return []
        ans = []
        for ii in range(0, len(s) + 1):
            base = s[:ii]
            if is_palindrome(base) and base != "":
                if not len(s[ii:]):
                    ans.append([base])
                else:
                    for part in self.get_partition(s[ii:]):
                        ans.append([base] + part)
        return ans


def partition(s: str) -> List[List[str]]:
    p = PalindromePartition()
    return p.partition(s)


print(partition("aab"))
