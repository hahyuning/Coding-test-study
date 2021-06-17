n, m = map(int, input().split())
dist1 = [[1e9] * (n + 1) for _ in range(n + 1)]
dist2 = [[1e9] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    dist1[a][b] = 1
    dist2[b][a] = 1

for i in range(1, n + 1):
    dist1[i][i] = 0
    dist2[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist1[i][j] = min(dist1[i][j], dist1[i][k] + dist1[k][j])
            dist2[i][j] = min(dist2[i][j], dist2[i][k] + dist2[k][j])

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if dist1[a][b] == 1e9 and dist2[a][b] == 1e9:
        print(0)
    elif dist1[a][b] == 1e9:
        print(1)
    elif dist2[a][b] == 1e9:
        print(-1)