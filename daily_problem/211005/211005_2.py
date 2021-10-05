from collections import deque

n = int(input())
a = list(map(int, input().split()))
a.sort()
a = deque(a)

ans = 0
while a:
    if len(a) == 1:
        ans += a[0]
        break
    x = a.popleft()
    y = a.pop()
    ans += y * 2
print(ans)