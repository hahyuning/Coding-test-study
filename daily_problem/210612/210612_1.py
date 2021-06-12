n = int(input())
a = list(map(int, input().split()))
a.sort()

lt = 0
rt = n - 1
min_val = a[lt] + a[rt]
p1, p2 = lt, rt
while lt < rt:
    tmp = a[lt] + a[rt]
    if tmp == 0:
        p1 = lt
        p2 = rt
        break

    if abs(tmp) < abs(min_val):
        min_val = tmp
        p1 = lt
        p2 = rt

    if tmp < 0:
        lt += 1
    else:
        rt -= 1

print(a[p1], a[p2])

