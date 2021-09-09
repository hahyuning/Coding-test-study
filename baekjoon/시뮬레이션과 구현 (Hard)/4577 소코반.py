def check(a):
    for i in range(n):
        for j in range(m):
            if a[i][j] == "+":
                return False
            if a[i][j] == "b":
                return False
    return True

tc = 0
while True:
    tc += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    # . 빈공간, # 벽, + 비어 있는 목표점, b 박스, B 목표점 위에 있는 박스
    # w 캐릭터, W 목표점 위에 있는 캐릭터
    a = [list(input()) for _ in range(n)]
    order = input()

    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == "w" or a[i][j] == "W":
                x, y = i, j

    d = {"U":(-1, 0), "D":(1, 0), "L":(0, -1), "R":(0, 1)}
    for i in order:
        nx, ny = x + d[i][0], y + d[i][1]

        # 빈 공간인 경우
        if a[nx][ny] == ".":
            a[nx][ny] = "w"
            if a[x][y] == "w":
                a[x][y] = "."
            else:
                a[x][y] = "+"
            x, y = nx, ny
        # 비어 있는 목표점인 경우
        elif a[nx][ny] == "+":
            a[nx][ny] = "W"
            if a[x][y] == "w":
                a[x][y] = "."
            else:
                a[x][y] = "+"
            x, ly = nx, ny

        # 박스인 경우
        if a[nx][ny] in ["b", "B"]:
            # 박스가 이동할 수 있는지 검사
            ch = False
            nnx, nny = nx + d[i][0], ny + d[i][1]

            # 이동할 수 없는 경우
            if a[nnx][nny] in ["#", "b", "B"]:
                ch = True

            if not ch:
                if a[nnx][nny] == ".":
                    a[nnx][nny] = "b"
                elif a[nnx][nny] == "+":
                    a[nnx][nny] = "B"

                if a[nx][ny] == "b":
                    a[nx][ny] = "w"
                else:
                    a[nx][ny] = "W"

                if a[x][y] == "w":
                    a[x][y] = "."
                else:
                    a[x][y] = "+"

                x, y = nx, ny

        if check(a):
            print("Game {}: complete".format(tc))
            for row in a:
                print("".join(row))
            break
    else:
        print("Game {}: incomplete".format(tc))
        for row in a:
            print("".join(row))