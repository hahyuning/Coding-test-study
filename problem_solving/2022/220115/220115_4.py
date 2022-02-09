def star(level, x, y):
    if level == 1:
        ans[x][y] = "*"
        return

    len = 4 * level - 3
    for i in range(len):
        ans[x][y + i] = "*"
        ans[x + len - 1][y + i] = "*"
        ans[x + i][y] = "*"
        ans[x + i][y + len - 1] = "*"

    star(level - 1, x + 2, y + 2)

n = int(input())
ans = [[" " for _ in range(4 * n - 3)] for _ in range(4 * n - 3)]

star(n, 0, 0)
for row in ans:
    print("".join(row))
