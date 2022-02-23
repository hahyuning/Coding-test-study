import sys
input = sys.stdin.readline


n, r = map(int, input().split())
cities = input().rstrip().split()

mapping = dict()
i = 0
for city in cities:
    if city not in mapping:
        mapping[city] = i
        i += 1
n = i

m = int(input())
route = input().split()

k = int(input())
cost = [[1e9] * n for _ in range(n)]
free_pass = [[1e9] * n for _ in range(n)]

for i in range(n):
    cost[i][i] = 0
    free_pass[i][i] = 0

for _ in range(k):
    x = input().rstrip().split()
    a, b = mapping[x[1]], mapping[x[2]]
    x[3] = float(x[3])
    cost[a][b] = min(cost[a][b], x[3])
    cost[b][a] = min(cost[b][a], x[3])

    if x[0] in ["ITX-Saemaeul", "ITX-Cheongchun", "Mugunghwa"]:
        free_pass[a][b] = 0
        free_pass[b][a] = 0
    elif x[0] in ["V-Train", "S-Train"]:
        free_pass[a][b] = min(free_pass[a][b], x[3] / 2)
        free_pass[b][a] = min(free_pass[b][a], x[3] / 2)
    else:
        free_pass[a][b] = min(free_pass[a][b], x[3])
        free_pass[b][a] = min(free_pass[b][a], x[3])

for c in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][c] + cost[c][j])
            free_pass[i][j] = min(free_pass[i][j], free_pass[i][c] + free_pass[c][j])

c1, c2 = 0, r
for i in range(m - 1):
    a, b = mapping[route[i]], mapping[route[i + 1]]
    c1 += cost[a][b]
    c2 += free_pass[a][b]

if c2 < c1:
    print("Yes")
else:
    print("No")