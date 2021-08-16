from collections import deque
import sys
input = sys.stdin.readline

n, t = map(int, input().split())
a = [(0, 0)]
for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

a.sort(key=lambda x:(x[1], x[0]))
q = deque()
dist = dict()
q.append((0, 0, 0))
dist[(0, 0)] = 0

while q:
    x, y, idx = q.popleft()
    for i in range(idx + 1, n + 1):
        nx, ny = a[i]
        if abs(nx - x) <= 2 and abs(ny - y) <= 2 and (nx, ny) not in dist:
            if ny == t:
                print(dist[(x, y)] + 1)
                sys.exit(0)

            dist[(nx, ny)] = dist[(x, y)] + 1
            q.append((nx, ny, i))
        elif abs(nx - x) > 2 and abs(ny - y) > 2:
            break
    for i in range(idx - 1, -1, -1):
        nx, ny = a[i]
        if abs(nx - x) <= 2 and abs(ny - y) <= 2 and (nx, ny) not in dist:
            if ny == t:
                print(dist[(x, y)] + 1)
                sys.exit(0)

            dist[(nx, ny)] = dist[(x, y)] + 1
            q.append((nx, ny, i))
        elif abs(nx - x) > 2 and abs(ny - y) > 2:
            break
print(-1)
