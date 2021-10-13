n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort()

left = a[0][0]
right = a[0][1]
ans = 0
for s, e in a:
    if s <= right:
        right = max(right, e)
    else:
        ans += (right - left)
        right = e
        left = s

ans += (right - left)
print(ans)