import sys

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    lt = 0
    rt = n - 1
    ans = []
    near = sys.maxsize
    while lt < rt:
        tmp = a[lt] + a[rt]
        if tmp == k:
            if near == 0:
                ans.append((lt, rt))
            else:
                ans = [(lt, rt)]
                near = 0
            lt += 1
            rt -= 1
        elif tmp > k:
            if tmp - k < near:
                near = tmp - k
                ans = [(lt, rt)]
            elif tmp - k == near:
                ans.append((lt, rt))
            rt -= 1
        else:
            if k - tmp < near:
                near = k - tmp
                ans = [(lt, rt)]
            elif k - tmp == near:
                ans.append((lt, rt))
            lt += 1
    print(len(ans))