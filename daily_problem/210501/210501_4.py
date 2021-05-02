from collections import deque

n, k = map(int, input().split())

q = deque([i for i in range(1, n + 1)])
ans = []

cnt = 0
while q:
    cnt += 1
    x = q.popleft()
    if cnt % k == 0:
        ans.append(x)
    else:
        q.append(x)

print("<" + ", ".join(map(str, ans)) + ">")