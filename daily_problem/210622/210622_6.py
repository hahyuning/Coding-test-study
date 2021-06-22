n = int(input())
dist = [[1e9] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dist[a][b] = 1
    dist[b][a] = 1

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dist[a][b] = min(dist[a][k] + dist[k][b], dist[a][b])

ans = []
for i in range(1, n + 1):
    tmp = max(dist[i][1:])
    ans.append((tmp, i))
ans.sort()

min_val = ans[0][0]
cnt = 0
min_list = []
for x, y in ans:
    if x == min_val:
        cnt += 1
        min_list.append(y)

print(min_val, cnt)
print(*min_list)