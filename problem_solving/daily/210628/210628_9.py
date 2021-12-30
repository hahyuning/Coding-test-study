from bisect import bisect_left

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = int(input())
    b = list(map(int, input().split()))

    for x in b:
        idx = bisect_left(a, x)
        if idx >= n:
            print(0)
        else:
            if a[idx] == x:
                print(1)
            else:
                print(0)