from bisect import bisect_left
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
points = list(map(int, input().split()))
points.sort()
for _ in range(m):
    s, e = map(int, input().split())
    s_id = bisect_left(points, s)
    e_id = bisect_left(points, e)
    if e_id < n and points[e_id] == e:
        print(e_id  - s_id + 1)
    else:
        print(e_id - s_id)