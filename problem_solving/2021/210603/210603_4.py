n = int(input())
dist = [[1e9] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for i in range(n):
    s = input()
    for j in range(n):
        if s[j] == "Y":
            dist[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

max_cnt = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if dist[i][j] != 0 and dist[i][j] <= 2:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)


