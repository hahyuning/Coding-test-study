n = int(input())

dist = [[1e9] * (26) for _ in range(26)]
for i in range(26):
    dist[i][i] = 0

for _ in range(n):
    a, b = input().split(" is ")
    a = ord(a) - ord("a")
    b = ord(b) - ord("a")
    dist[a][b] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

m = int(input())
for _ in range(m):
    a, b = input().split(" is ")
    a = ord(a) - ord("a")
    b = ord(b) - ord("a")
    if dist[a][b] != 1e9:
        print("T")
    else:
        print("F")

