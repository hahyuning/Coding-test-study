import sys

s, c = map(int, input().split())
l = [int(input()) for _ in range(s)]

lt = 0
rt = 1000000000
ans = sys.maxsize
while lt <= rt:
    mid = (lt + rt) // 2
    if max(l) < mid:
        rt = mid - 1
        continue

    cnt = 0
    for x in l:
        cnt += x // mid

    if cnt >= c:
        ans = min(ans, sum(l) - mid * c)
        lt = mid + 1
    else:
        rt = mid - 1
print(ans)
