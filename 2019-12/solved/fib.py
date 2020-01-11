class FibClass:
    """
        Illustration of how much memoization improves algorithm perfromance
        Also shows a bottomup solution that is even better, as no recursion at all is needed
        fib_recur --> O(2^n)
        fib_memo --> O(n)
        fib_bottomup --> O(n)
    """

    memo = {}
    recur_depth = 0
    memo_depth = 0

    def fib_recur(self, n):
        self.recur_depth += 1
        if n == 0 or n == 1:
            return 1
        else:
            return self.fib_recur(n - 1) + self.fib_recur(n - 2)

    def fib_memo(self, n):
        self.memo_depth += 1
        mem_hit = self.memo.get(n)
        if mem_hit:
            return mem_hit
        else:
            if n == 0 or n == 1:
                return 1
            else:
                self.memo[n] = self.fib_memo(n - 1) + self.fib_memo(n - 2)
                return self.memo[n]

    def fib_bottomup(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            temp = None
            first = 1
            second = 1
            for i in range(n - 1):
                temp = second
                second += first
                first = temp
            return second


if __name__ == "__main__":
    test_case = FibClass()
    n = 20
    print(
        f"fib_recur({n}) = {test_case.fib_recur(n)} (Recursion Depth:{test_case.recur_depth})"
    )
    print(
        f"fib_memo({n}) = {test_case.fib_memo(n)} (Recursion Depth:{test_case.memo_depth})"
    )
    print(f"fib_bottomup({n}) = {test_case.fib_bottomup(n)}")
