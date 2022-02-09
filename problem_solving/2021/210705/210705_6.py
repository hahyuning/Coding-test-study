def check(mid):
    res = 0
    prev = -mid
    for x, y in wrong:
        if prev + mid - 1 < y:
            res += 1
            prev = y
    return res

n, m = map(int, input().split())
limit = int(input())
k = int(input())
wrong = []
min_h = 0
for _ in range(k):
    a, b = map(int, input().split())
    min_h = max(min_h, a)
    wrong.append((a, b))
wrong.sort(key=lambda x:x[1])

lt = min_h
rt = n
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    res = check(mid)
    if res > limit:
        lt = mid + 1
    else:
        rt = mid - 1
        ans = mid
print(ans)
