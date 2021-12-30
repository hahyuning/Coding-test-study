import sys
INF = sys.maxsize

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dist = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            dist[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]


for i in range(n):
    for j in range(n):
        if dist[i][j] != INF:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()