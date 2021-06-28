n = int(input())
a = list(map(int, input().split()))
a.sort()

res = []
min_diff = 3 * (10 ** 9)
for i in range(len(a) - 2):
    lt = i + 1
    rt = len(a) - 1

    while lt < rt:
        tmp = a[i] + a[lt] + a[rt]
        if tmp < 0:
            if abs(tmp) < min_diff:
                min_diff = abs(tmp)
                res = [a[i], a[lt], a[rt]]
            lt += 1
        elif tmp > 0:
            if abs(tmp) < min_diff:
                min_diff = abs(tmp)
                res = [a[i], a[lt], a[rt]]
            rt -= 1
        else:
            res = [a[i], a[lt], a[rt]]
            break

print(*res)

