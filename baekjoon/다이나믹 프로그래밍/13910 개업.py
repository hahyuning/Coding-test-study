import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
s = list(map(int, input().split()))

for i in range(m):
    for j in range(i, m):
        if i == j:
            continue
        else:
            if s[i] + s[j] <= n and s[i] + s[j] not in s:
                s.append(s[i] + s[j])

s.sort()
# d[i]: i개의 짜장면을 만들기 위해 해야하는 최소 요리 횟수
# d[i] = min(d[i - s[j]]) + 1, 0 <= j < len(s)
d = [INF] * (n + 1)
d[0] = 0

for i in range(1, n + 1):
    for x in s:
        if i - x >= 0:
            d[i] = min(d[i], d[i - x] + 1)
        else:
            break

if d[n] == INF:
    print(-1)
else:
    print(d[n])