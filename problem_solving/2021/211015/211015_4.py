from collections import deque

n, l = map(int, input().split())
a = list(map(int, input().split()))
q = deque()

for i in range(n):
    x = a[i]

    while q and q[-1] > x:
        q.pop()
    q.append(x)

    if i >= l and q[0] == a[i - l]:
        q.popleft()
    print(q[0], end=" ")