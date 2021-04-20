def check(a, start_row, end_row, start_col, end_col):
    n = len(a)
    ans = 1

    # 가로 방향 확인
    for i in range(start_row, end_row + 1):
        cnt = 1
        for j in range(1, n):
            if a[i][j] == a[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)

    # 세로 방향 확인
    for j in range(start_col, end_col + 1):
        cnt = 1
        for i in range(1, n):
            if a[i][j] == a[i - 1][j]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
    return ans

n = int(input())
a = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
            tmp = check(a, i, i, j, j + 1)
            ans = max(ans, tmp)
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]

        if j + 1 < n:
            a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
            tmp = check(a, i, i + 1, j, j)
            ans = max(ans, tmp)
            a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]

print(ans)