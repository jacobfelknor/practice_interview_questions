def check_power_three(n: int) -> int:
    if n == 0:
        return False, 0, []
    powers = []
    ii = 0
    while 3**ii <= n:
        ii+=1
    ii -= 1 # went one step too far, back up once
    # now, substract 3**ii from n
    n -= 3**ii
    powers.append(ii)
    # i now have highest power of 3 in the list
    # from here, decrease powers of 3 and add to powers if they fit
    ii -= 1
    while ii >= 0:
        if 3**ii <= n:
            powers.append(ii)
            n -= 3**ii
        ii -= 1
    
    return n == 0, n, powers


def is_power_three(n: int) -> int:
    ii = 0
    while True:
        if 3**ii > n:
            return False
        if 3**ii == n:
            return True
        ii += 1


n = 3**0 + 3**6 + 3**12 + 3**16 + 3**2 + 3**3 + 3**9 + 3**1
print(check_power_three(n))


assert is_power_three(3**4)
assert not is_power_three(21)