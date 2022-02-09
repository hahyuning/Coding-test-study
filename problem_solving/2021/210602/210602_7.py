import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            dist[a][b] = min(dist[a][k] + dist[k][b], dist[a][b])

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if dist[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")