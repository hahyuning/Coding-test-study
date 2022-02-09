n = int(input())
m = int(input())
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

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if dist1[i][j] == 1e9 and dist2[i][j] == 1e9:
            cnt += 1
    print(cnt)

