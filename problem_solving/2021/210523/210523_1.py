import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))

# d[i]: i번째 수까지의 합
d = [0] * (n + 1)
for i in range(1, n + 1):
    d[i] = d[i - 1] + a[i]

for _ in range(m):
    i, j = map(int, input().split())
    print(d[j] - d[i - 1])