import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = INF
h = 0
for k in range(257):
    plus = 0
    minus = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] > k:
                plus += a[i][j] - k
            else:
                minus += k - a[i][j]
    time = 2 * plus + minus
    if plus - minus + b < 0:
        continue

    if time <= ans:
        ans = time
        h = k
print(ans, h)

