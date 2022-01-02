dx = [-1, -1, 1, 1]
dy = [1, -1, 1, -1]

def backtracking(i, j, bishop):
    for k in range(4):
        x, y = i + dx[k], j + dy[k]
        while 0 <= x < n and 0 <= y < n:
            if (x, y) in bishop:
                return False
            x += dx[k]
            y += dy[k]
    return True

def check1(sx, sy, bishop1):
    global ans1
    if backtracking(sx, sy, bishop1):
        ans1 = max(len(bishop1), ans1)
    else:
        return

    for i in range(sx, n):
        if i % 2 == 0:
            for j in range(0, n, 2):
                if a[i][j] == 1 and not ch[i][j]:
                    ch[i][j] = True
                    bishop1.append((i, j))
                    check1(i, j, bishop1)
                    bishop1.pop()
                    ch[i][j] = False
        else:
            for j in range(1, n, 2):
                if a[i][j] == 1 and not ch[i][j]:
                    ch[i][j] = True
                    bishop1.append((i, j))
                    check1(i, j, bishop1)
                    bishop1.pop()
                    ch[i][j] = False

def check2(sx, sy, bishop2):
    global ans2
    if backtracking(sx, sy, bishop2):
        ans2 = max(len(bishop2), ans2)
    else:
        return

    for i in range(sx, n):
        if i % 2 == 0:
            for j in range(1, n, 2):
                if a[i][j] == 1 and not ch[i][j]:
                    ch[i][j] = True
                    bishop2.append((i, j))
                    check2(i, j, bishop2)
                    bishop2.pop()
                    ch[i][j] = False
        else:
            for j in range(0, n, 2):
                if a[i][j] == 1 and not ch[i][j]:
                    ch[i][j] = True
                    bishop2.append((i, j))
                    check2(i, j, bishop2)
                    bishop2.pop()
                    ch[i][j] = False

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans1 = 0
ans2 = 0
ch = [[False] * n for _ in range(n)]
check1(0, 0, [])
check2(0, 0, [])
print(ans1 + ans2)