def sudoku(n):
    # 종료 조건: 모든 칸을 다 탐색한 경우
    if n == 81:
        for x in a:
            print(" ".join(map(str, x)))
        return True

    i = n // 9
    j = n % 9

    if a[i][j] != 0:
        return sudoku(n + 1)
    else:
        for k in range(1, 10):
            if check_horizontal[i][k] == False and check_vertical[j][k] == False and check_square[3 * (i // 3) + (j // 3)][k] == False:
                check_horizontal[i][k] = True
                check_vertical[j][k] = True
                check_square[3 * (i // 3) + (j // 3)][k] = True
                a[i][j] = k
                if sudoku(n + 1):
                    return True
                # 잘못된 스도쿠였을 경우
                check_horizontal[i][k] = False
                check_vertical[j][k] = False
                check_square[3 * (i // 3) + (j // 3)][k] = False
                a[i][j] = 0
    return False

a = [list(map(int, input().split())) for _ in range(9)]
check_horizontal = [[False] * 10 for _ in range(9)]
check_vertical = [[False] * 10 for _ in range(9)]
check_square = [[False] * 10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if a[i][j] != 0:
            check_horizontal[i][a[i][j]] = True
            check_vertical[j][a[i][j]] = True
            check_square[3 * (i // 3) + (j // 3)][a[i][j]] = True

sudoku(0)
