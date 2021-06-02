import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def find_path(i, j):
    if path[i][j] == 0:
        return []

    k = path[i][j]
    return find_path(i, k) + [k] + find_path(k, j)

n, m = map(int, input().split())
dist = [[1e9] * (n + 1) for _ in range(n + 1)]
path = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = c
    dist[b][a] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for c in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if dist[a][c] + dist[c][b] < dist[a][b]:
                dist[a][b] = dist[a][c] + dist[c][b]
                path[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print("-", end=" ")
            continue

        p = find_path(i, j)
        if len(p) == 0:
            print(j, end=" ")
        else:
            print(p[0], end=" ")
    print()