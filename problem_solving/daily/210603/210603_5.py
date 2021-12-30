n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

check = True
for i in range(n):
    for j in range(m):
        if a[i][j] == "W":
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == "S":
                        check = False
                        break
                    elif a[nx][ny] == ".":
                        a[nx][ny] = "D"

        if not check:
            break
    if not check:
        break

if not check:
    print(0)
else:
    print(1)
    for row in a:
        print("".join(row))