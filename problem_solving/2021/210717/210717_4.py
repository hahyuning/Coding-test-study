def solution(l, x, y):
    global cnt1, cnt2
    if n == 1:
        if a[x][y] == 0:
            cnt1 += 1
        else:
            cnt2 += 1
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
        solution(l // 2, x, y)
        solution(l // 2, x + l // 2, y)
        solution(l // 2, x, y + l // 2)
        solution(l // 2, x + l // 2, y + l // 2)
    else:
        if color == 0:
            cnt1 += 1
        else:
            cnt2 += 1

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
cnt1 = 0
cnt2 = 0
solution(n, 0, 0)
print(cnt1)
print(cnt2)