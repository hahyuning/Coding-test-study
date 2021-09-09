import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INF = sys.maxsize

def find_path(i, j):
    if trace[i][j] == 0:
        return []

    k = trace[i][j]
    return find_path(i, k) + [k] + find_path(k, j)

n = int(input())
m = int(input())
dist = [[INF] * (n + 1) for _ in range(n + 1)]
trace = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                trace[i][j] = k

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] != INF:
            print(dist[i][j], end=" ")
        else:
            print(0, end=" ")
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == 0 or dist[i][j] == INF:
            print(0)
            continue

        path = [i] + find_path(i, j) + [j]
        print(len(path), end=" ")
        print(*path)