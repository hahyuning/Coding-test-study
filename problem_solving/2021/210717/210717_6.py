def solution(l, x, y):
    global ans
    if n == 1:
        ans += a[x][y]
        return

    check = False
    color = a[x][y]
    for i in range(x, x + l):
        for j in range(y, y + l - 1):
            if a[i][j] != a[i][j + 1]:
                check = True
                break
        if check:
            break

    for j in range(y, y + l):
        for i in range(x, x + l - 1):
            if a[i][j] != a[i + 1][j]:
                check = True
                break
        if check:
            break

    if check:
        ans += "("
        solution(l // 2, x, y)
        solution(l // 2, x, y + l // 2)
        solution(l // 2, x + l // 2, y)
        solution(l // 2, x + l // 2, y + l // 2)
        ans += ")"
    else:
        ans += color

n = int(input())
a = [input() for _ in range(n)]
ans = ""
solution(n, 0, 0)
print(ans)
