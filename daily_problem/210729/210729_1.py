from bisect import bisect_right

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(1, n):
    b.append(b[-1] + a[i])

if k <= b[-1]:
    print(bisect_right(b, k) + 1)
else:
    k -= b[-1]
    max_val = b[-1]
    c = []
    for i in range(n - 1, -1, -1):
        c.append(max_val - b[i])
    ans = n - bisect_right(c, k)
    if k == c[ans]:
        print(ans)
    else:
        print(ans + 1)