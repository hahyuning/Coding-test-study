def solution(n):
    ans = 0
    while n != 0:
        a, b = divmod(n, 2)
        ans += b
        n = a
    return ans