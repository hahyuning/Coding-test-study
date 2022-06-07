from itertools import permutations

n, start = map(int, input().split())
dist = [[1001] * n for _ in range(n)]

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        dist[i][j] = a[j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

b = [i for i in range(n) if i != start]
pmt = permutations(b)
ans = -1
for route in pmt:
    time = 0
    for i in range(n - 1):
        if i == 0:
            time += dist[start][route[i]]
        else:
            time += dist[route[i - 1]][route[i]]

    if ans == -1 or time < ans:
        ans = time

print(ans)