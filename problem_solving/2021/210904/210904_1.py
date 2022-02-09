n = int(input())
a = [input() for _ in range(n)]
b = [input() for _ in range(n)]

ans = [["."] * n for _ in range(n)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

check = False
for i in range(n):
    for j in range(n):
        if a[i][j] == "." and b[i][j] == "x":
            cnt = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == "*":
                    cnt += 1
            ans[i][j] = str(cnt)

        if a[i][j] == "*" and b[i][j] == "x":
            check = True

if check:
    for i in range(n):
        for j in range(n):
            if a[i][j] == "*":
                ans[i][j] = "*"

for row in ans:
    print("".join(row))
