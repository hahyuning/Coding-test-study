from collections import deque

n = int(input())
a = list(map(int, input().split()))
a.sort()

a = deque(a)
while len(a) > 1:
    x = a.popleft()
    y = a.pop()
    a.append(y + x / 2)

ans = a[0]
if int(ans) == ans:
    print(int(ans))
else:
    print(ans)