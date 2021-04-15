from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    maps = [["."] + list(input()) for _ in range(n)]

    x1 = y1 = x2 = y2 = -1
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "&":
                if x1 == -1:
                    x1, y1 = i, j
                else:
                    x2, y2 = i, j



