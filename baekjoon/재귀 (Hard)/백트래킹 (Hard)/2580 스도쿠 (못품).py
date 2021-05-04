def sdoku(z):
    if z == 81:
        for row in a:
            print(' '.join(map(str, row)))
        return True
    x = z // n
    y = z % n
    if a[x][y] != 0:
        return sdoku(z + 1)
    else:
        for i in range(1, 10):
            if c[x][i] == False and c2[y][i] == False and c3[(x // 3) * 3 + (y // 3)][i] == False:
                c[x][i] = c2[y][i] = c3[(x // 3) * 3 + (y // 3)][i] = True
                a[x][y] = i
                if sdoku(z + 1):
                    return True
                a[x][y] = 0
                c[x][i] = c2[y][i] = c3[(x // 3) * 3 + (y // 3)][i] = False
    return False


n = 9
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * 10 for _ in range(n)]
c2 = [[False] * 10 for _ in range(n)]
c3 = [[False] * 10 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            c[i][a[i][j]] = True
            c2[j][a[i][j]] = True
            c3[(i // 3) * 3 + (j // 3)][a[i][j]] = True
sdoku(0)
