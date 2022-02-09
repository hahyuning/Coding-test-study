import sys

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

lt = 0
rt = lt + 1

ans = sys.maxsize
while lt < n and rt < n:
    tmp = a[rt] - a[lt]
    if tmp >= m:
        ans = min(ans, tmp)
        lt += 1

        if lt > rt:
            rt = lt + 1
    else:
        rt += 1
print(ans)