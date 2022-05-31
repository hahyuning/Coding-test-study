n = int(input())
board = [[False] * 100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = True

ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j]:
            ans += 1
print(ans)