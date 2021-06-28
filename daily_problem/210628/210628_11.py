def check(x):
    res = 0
    for y in l:
        res += y // x
    return res

s, c = map(int, input().split())
l = [int(input()) for _ in range(s)]

lt = 0
rt = max(l) - 1
ans = 0
cnt = 0
while lt <= rt:
    mid = (lt + rt) // 2
    res = check(mid)
    if res >= c:
        ans = mid
        cnt = res
        lt = mid + 1
    else:
        rt = mid - 1

print(sum(l) - cnt * ans)

