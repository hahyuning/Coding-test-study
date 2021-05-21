from collections import deque

n, m = map(int, input().split())
target = list(map(int, input().split()))
ans = 0

q = deque([i for i in range(1, n + 1)])
for num in target:
    if q[0] == num:
        q.popleft()
        continue

    i = q.index(num)
    if i <= len(q) // 2:
        ans += i
        for _ in range(i):
            q.append(q.popleft())
        q.popleft()
    else:
        ans += (len(q) - i)
        for _ in range(len(q) - i):
            q.appendleft(q.pop())
        q.popleft()

print(ans)