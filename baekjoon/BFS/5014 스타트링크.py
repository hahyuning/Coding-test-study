from collections import deque

# f: 건물의 높이, s: 시작 위치, g: 목적지 위치, u: 위로 u층, d: 아래로 d층
f, s, g, u, d = map(int, input().split())
check = [-1] * (f + 1)
q = deque()
q.append(s)
check[s] = 0

while q:
    now = q.popleft()
    for next in [now + u, now - d]:
        if 1 <= next <= f and check[next] == -1:
            q.append(next)
            check[next] = check[now] + 1

if check[g] == -1:
    print("use the stairs")
else:
    print(check[g])