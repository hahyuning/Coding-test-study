def check(m, n, a):
    check = [[0] * n for _ in range(m)]

    # 사각형이 같은 모양인지 확인
    for i in range(m - 1):
        for j in range(n - 1):
            if a[i][j] != "." and a[i][j] == a[i + 1][j] == a[i][j + 1] == a[i + 1][j + 1]:
                check[i][j] += 1
                check[i + 1][j] += 1
                check[i][j + 1] += 1
                check[i + 1][j + 1] += 1

    # 지워지는 칸 .로 표시
    cnt = 0
    for i in range(m):
        for j in range(n):
            if check[i][j] > 0:
                cnt += 1
                a[i][j] = "."

    return a, cnt

def move(m, n, a):
    for j in range(n):
        tmp = []
        for i in range(m - 1, -1, -1):
            if a[i][j] != ".":
                tmp.append(a[i][j])

        while len(tmp) < m:
            tmp.append(".")
        tmp.reverse()

        for i in range(m):
            a[i][j] = tmp[i]

    return a

def solution(m, n, board):
    ans = 0
    board = [list(x) for x in board]

    while True:
        # 1. 지워질 블록 구하기
        board, cnt = check(m, n, board)
        if cnt == 0:
            break
        ans += cnt

        # 2. 블록 떨어트리기
        board = move(m, n, board)

    return ans
