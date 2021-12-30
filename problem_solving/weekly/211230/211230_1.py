def rotate(sticker, a, b):
    result = [[0 for _ in range(a)] for _ in range(b)]
    for i in range(b):
        for j in range(a):
            result[i][j] = sticker[a - j - 1][i]
    return result

def check():
    global board
    row, col = len(sticker), len(sticker[0])

    for i in range(n - row + 1):
        for j in range(m - col + 1):
            duplicated = False
            for k in range(row):
                for l in range(col):
                    board[i + k][j + l] += sticker[k][l]

                    if board[i + k][j + l] == 2:
                        duplicated = True
            if duplicated:
                for k in range(row):
                    for l in range(col):
                        board[i + k][j + l] -= sticker[k][l]
            else:
                return True
    return False


n, m, k = map(int, input().split())
stickers = []
for _ in range(k):
    a, b = map(int, input().split())
    tmp = [list(map(int, input().split())) for _ in range(a)]
    stickers.append(tmp)

board = [[0 for _ in range(m)] for _ in range(n)]
ans = 0

for i in range(k):
    sticker = stickers[i]

    for j in range(4):
        if check():
            break
        sticker = rotate(sticker, len(sticker), len(sticker[0]))

for i in range(n):
    for j in range(m):
        if board[i][j]:
            ans += 1

print(ans)