board = [input() for _ in range(8)]
ans = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and board[i][j] == "F":
            ans += 1
        if i % 2 == 1 and j % 2 == 1 and board[i][j] == "F":
            ans += 1
print(ans)