def solution(l, x, y):
    global cnt1, cnt2, cnt3
    if n == 1:
        if a[x][y] == -1:
            cnt1 += 1
        elif a[x][y] == 0:
            cnt2 += 1
        else:
            cnt3 += 1
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
        solution(l // 3, x, y)
        solution(l // 3, x + l // 3, y)
        solution(l // 3, x + l // 3 * 2, y)
        solution(l // 3, x, y + l // 3)
        solution(l // 3, x, y + l // 3 * 2)
        solution(l // 3, x + l // 3, y + l // 3)
        solution(l // 3, x + l // 3 * 2, y + l // 3)
        solution(l // 3, x + l // 3, y + l // 3 * 2)
        solution(l // 3, x + l // 3 * 2, y + l // 3 * 2)
    else:
        if color == -1:
            cnt1 += 1
        elif color == 0:
            cnt2 += 1
        else:
            cnt3 += 1

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
cnt1 = 0
cnt2 = 0
cnt3 = 0
solution(n, 0, 0)
print(cnt1)
print(cnt2)
print(cnt3)