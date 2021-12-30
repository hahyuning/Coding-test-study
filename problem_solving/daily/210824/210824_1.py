from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 0
for rt in range(n - 1, -1, -1):
    lt = bisect_left(a, a[rt] * 0.9)
    ans += (rt - lt)
print(ans)