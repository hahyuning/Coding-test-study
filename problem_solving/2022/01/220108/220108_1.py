n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        check = False
        for x in range(m):
            for y in range(m):
                if a[i][x] < a[i][y] and a[j][x] >= a[j][y]:
                    check = True
                if a[i][x] > a[i][y] and a[j][x] <= a[j][y]:
                    check = True
                if a[i][x] == a[i][y] and a[j][x] != a[j][y]:
                    check = True

        if not check:
            ans += 1
print(ans)