n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n - 2):
    if a[i] > 0:
        break

    lt, rt = i + 1, n - 1
    while lt < rt:
        sum = a[i] + a[lt] + a[rt]
        if sum < 0:
            lt += 1
        elif sum > 0:
            rt -= 1
        else:
            if a[lt] == a[rt]:
                ans += (rt - lt + 1) * (rt - lt) // 2
                break

            c1 = 1
            c2 = 1
            while lt < rt and a[lt] == a[lt + 1]:
                c1 += 1
                lt += 1
            while lt < rt and a[rt] == a[rt - 1]:
                c2 += 1
                rt -= 1

            ans += (c2 * c1)
            lt += 1
            rt -= 1
print(ans)