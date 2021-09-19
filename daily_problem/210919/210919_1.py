import sys
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
d = [0] * (n + 1)

for i in range(1, n):
    if a[i] > a[i + 1]:
        d[i] = 1

for i in range(1, n + 1):
    d[i] += d[i - 1]

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    print(d[y - 1] - d[x - 1])