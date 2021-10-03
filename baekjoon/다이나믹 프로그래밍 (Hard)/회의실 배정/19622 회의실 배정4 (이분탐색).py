from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
a = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x:x[1])
end_time = [x[1] for x in a]

# d[i]: i번째 회의까지 고려했을 때 회의 인원의 최대값
d = [0] * (n + 1)
d[1] = a[1][2]

for i in range(2, n + 1):
    s = a[i][0]
    idx = bisect_left(end_time, s)
    d[i] = max(d[i - 1], d[idx - 1] + a[i][2])

print(d[n])