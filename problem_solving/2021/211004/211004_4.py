n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]

ans = 0
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if a[i][j] == 1:
            ans += 1
            for x in range(i + 1):
                for y in range(j + 1):
                    a[x][y] = 1 - a[x][y]
print(ans)