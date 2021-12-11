n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))

for _ in range(m):
    op, l, r = map(int, input().split())
    if op == 1:
        a[l] = r
    elif op == 2:
        for i in range(l, r + 1):
            a[i] = 1 - a[i]
    elif op == 3:
        for i in range(l, r + 1):
            a[i] = 0
    else:
        for i in range(l, r + 1):
            a[i] = 1

print(*a[1:])