from bisect import bisect_left

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    ans = 0
    for x in a:
        ans += bisect_left(b, x)

    print(ans)

