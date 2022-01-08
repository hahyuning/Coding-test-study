import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep = list(map(int, input().split()))
check = list(map(int, input().split()))
check.sort()

res = [False] * (n + 3)
for x in check:
    if x in sleep or res[x]:
        continue

    for y in range(x, n + 3, x):
        res[y] = True

for x in sleep:
    res[x] = False

sum = [0] * (n + 3)
for i in range(3, n + 3):
    if not res[i]:
        sum[i] = sum[i - 1] + 1
    else:
        sum[i] = sum[i - 1]

for _ in range(m):
    s, e = map(int, input().split())
    print(sum[e] - sum[s - 1])
