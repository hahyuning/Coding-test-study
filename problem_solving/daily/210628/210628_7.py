from bisect import bisect_left

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()
for _ in range(m):
    x = int(input())
    idx = bisect_left(a, x)
    if idx >= n:
        print(-1)
    else:
        if a[idx] == x:
            print(idx)
        else:
            print(-1)