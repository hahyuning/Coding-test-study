import sys

def solution(t, ans):
    if len(t) == 0:
        if len(ans) == n:
            print(" ".join(map(str, ans)))
            sys.exit(0)
        return

    if len(ans) > n:
        return

    x = int(t[0])
    if not check[x]:
        check[x] = True
        solution(t[1:], ans + [x])
        check[x] = False

    if len(t) >= 2:
        x = int(t[:2])
        if 10 <= x <= n and not check[x]:
            check[x] = True
            solution(t[2:], ans + [x])
            check[x] = False

s = input()
if len(s) <= 9:
    print(" ".join(list(s)))
else:
    m = len(s) - 9
    n = 9 + m // 2

    check = [False] * (n + 1)
    solution(s, [])