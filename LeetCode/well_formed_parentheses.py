"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]

"""


from typing import List
import time

# recursive
def generateParenthesis_recursive(n: int) -> List[str]:
    # Three cases I see
    # () + genHelper(n-1)
    # ( + genHelper(n-1) + )
    # genHelper(n-1) + ()
    if n == 1:
        return ["()"]
    else:
        sub_solutions = generateParenthesis_recursive(n - 1)
        this_solution = set()
        for solution in sub_solutions:
            this_solution.add("()" + solution)
            this_solution.add("(" + solution + ")")
            this_solution.add(solution + "()")
        return list(this_solution)


# DP Memo
# NOTE: subproblems are non-overlapping... Will never make use of my table :(
class GenerateParenthesis:
    def __init__(self) -> None:
        self.table = {}

    def subProblem(self, n: int) -> List[str]:
        if n in self.table:
            return self.table[n]
        else:
            ans = self.generateParenthesis(n)
            self.table[n] = ans
            return ans

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        else:
            sub_solutions = self.subProblem(n - 1)
            this_solution = set()
            for solution in sub_solutions:
                this_solution.add("()" + solution)
                this_solution.add("(" + solution + ")")
                this_solution.add(solution + "()")
            return list(this_solution)


def generateParenthesis(n: int) -> List[str]:
    # Three cases I see
    # () + genHelper(n-1)
    # ( + genHelper(n-1) + )
    # genHelper(n-1) + ()
    dp = GenerateParenthesis()
    return dp.generateParenthesis(n)


N = 17

t0 = time.time_ns()
generateParenthesis(N)
t1 = time.time_ns()

print(f"DP solution took {t1 - t0} nanoseconds")

t0 = time.time_ns()
generateParenthesis_recursive(N)
t1 = time.time_ns()

print(f"Recursive solution took {t1 - t0} nanoseconds")
