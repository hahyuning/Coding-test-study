import math

def base_change(num, base):
    T = "0123456789"

    n, d = divmod(num, base)
    if n == 0:
        return T[d]

    return base_change(n, base) + T[d]

def check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    ans = 0
    convert_n = base_change(n, k)
    zero_remove = convert_n.split("0")
    for x in zero_remove:
        if x == "" or x == "1":
            continue
        if check(int(x)):
            ans += 1

    return ans

solution(1000000, 9)