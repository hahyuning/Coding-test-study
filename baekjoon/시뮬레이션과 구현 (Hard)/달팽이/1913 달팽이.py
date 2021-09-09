n = int(input())
m = int(input())

a = [[0] * n for _ in range(n)]
x = (n - 1) // 2
y = (n - 1) // 2
a[x][y] = 1
num = 2

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for size in range(3, n + 1, 2):
    # 위로 한칸 이동
    x += dx[3]
    y += dy[3]
    a[x][y] = num
    num += 1

    for k in range(4):
        cnt = size - 1
        if k == 0:
            cnt -= 1
        for _ in range(cnt):
            x += dx[k]
            y += dy[k]
            a[x][y] = num
            num += 1

x = 0
y = 0
for idx, row in enumerate(a):
    print(*row)

    if m in row:
        x = idx + 1
        y = row.index(m) + 1

print(x, y)