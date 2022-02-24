from bisect import bisect_left

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    ans = 0
    for x in a:
        idx = bisect_left(b, x)
        if idx == 0:
            ans += b[0]
        elif idx == m:
            ans += b[-1]
        else:
            if abs(x - b[idx]) < abs(x - b[idx - 1]):
                ans += b[idx]
            else:
                ans += b[idx - 1]
    print(ans)