from itertools import permutations
import sys

n, m, h = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
route = []
sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            route.append((i, j))
        elif a[i][j] == 1:
            sx, sy = i, j

for i in range(len(route), -1, -1):
    routes = permutations(route, i)
    for r in routes:
        check = True
        power = m
        nx, ny = sx, sy
        for x, y in r:
            if abs(nx - x) + abs(ny - y) > power:
                check = False
                break

            power -= abs(nx - x) + abs(ny - y)
            power += h
            nx, ny = x, y
        else:
            if abs(nx - sx) + abs(ny - sy) > power:
                check = False

        if check:
            print(i)
            sys.exit(0)
print(-1)
