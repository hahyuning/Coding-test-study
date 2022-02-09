n = int(input())
a = [0] + list(map(int, input().split()))
m = int(input())
for _ in range(m):
    s, k = map(int, input().split())

    if s == 1:
        for i in range(k, n + 1, k):
            a[i] =  1 - a[i]
    else:
        lt = k
        rt = k
        while lt - 1 > 0 and rt + 1 <= n:
            if a[lt - 1] != a[rt + 1]:
                break
            lt -= 1
            rt += 1

        for i in range(lt, rt + 1):
            a[i] = 1 - a[i]

a = a[1:]
while len(a) >= 20:
    for i in range(20):
        print(a[i], end=" ")
    print()
    a = a[20:]
print(*a)
