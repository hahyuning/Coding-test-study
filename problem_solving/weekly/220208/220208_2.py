def count(x):
    cnt = 0
    for y in l:
        cnt += y // x
    return cnt


s, c = map(int, input().split())
l = [int(input()) for _ in range(s)]

lt = 1
rt = max(l)
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= c:
        ans = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(ans)