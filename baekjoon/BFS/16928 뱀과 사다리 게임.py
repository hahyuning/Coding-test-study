from collections import deque

n, m = map(int, input().split())

slide = dict()
for _ in range(n + m):
    s, e = map(int, input().split())
    slide[s] = e

check = [-1] * 101
check[1] = 0
q = deque()
q.append(1)

while q:
    now = q.popleft()

    for i in range(1, 7):
        if now + i > 100:
            continue

        if now + i in slide and check[slide[now + i]] == -1:
            check[slide[now + i]] = check[now] + 1
            check[now + i] = check[now] + 1
            q.append(slide[now + i])

        elif now + i not in slide and check[now + i] == -1:
            check[now + i] = check[now] + 1
            q.append(now + i)

print(check[100])