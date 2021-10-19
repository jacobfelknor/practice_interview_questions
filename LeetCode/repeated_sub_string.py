def repeatedSubstringPattern(s: str) -> bool:
        # length of substr has to be divisor of full string
        total_len = len(s)
        divisors = list(filter(lambda x: x is not None, (x if total_len % x == 0 else None for x in range(1, total_len // 2 + 1))))
        possible_strings = [s[:x]*(total_len//x) for x in divisors]
        return any(x == s for x in possible_strings)


s = "aadeaade"
print(repeatedSubstringPattern(s))
