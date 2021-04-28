n = int(input())
m = int(input())
dist = [[1e9] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            dist[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dist[a][b] = min(dist[a][k] + dist[k][b], dist[a][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if dist[a][b] != 1e9:
            print(dist[a][b], end=" ")
    print()

