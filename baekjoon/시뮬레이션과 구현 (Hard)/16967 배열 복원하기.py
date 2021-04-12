# a의 크기: h X w, b의 크기: (h + x) X (w + y)
h, w, x, y = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h + x)]

for i in range(h):
    for j in range(w):
        b[i + x][j + y] -= b[i][j]

for i in range(h):
    print(*b[i][:w])