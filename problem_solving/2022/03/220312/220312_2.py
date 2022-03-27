def solution(n, clockwise):
    ans = [[0] * n for _ in range(n)]
    x, y = n // 2, n // 2

    def rotate(a):
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[j][n - i - 1] = a[i][j]
        return res


    if clockwise:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        if n % 2 == 0:
            x -= 1

        for _ in range(4):
            ans = rotate(ans)
            i, j = 0, -1
            dir = 0
            num = n - 1
            now = 1
            while True:
                if i == x and j == y:
                    break
                for _ in range(num):
                    i += dx[dir]
                    j += dy[dir]
                    ans[i][j] = now
                    now += 1

                if num == 2:
                    num = 1
                else:
                    num -= 2
                dir = (dir + 1) % 4

    else:
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]

        if n % 2 == 0:
            y -= 1
        for _ in range(4):
            ans = rotate(ans)
            i, j = 0, n
            dir = 0
            num = n - 1
            now = 1
            while True:
                if i == x and j == y:
                    break
                for _ in range(num):
                    i += dx[dir]
                    j += dy[dir]
                    ans[i][j] = now
                    now += 1
                    print(i, j)
                if num == 2:
                    num = 1
                else:
                    num -= 2
                dir = (dir + 1) % 4

    return ans

solution(4, True)