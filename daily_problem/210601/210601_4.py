n, m = map(int, input().split())
board = [input() for _ in range(n)]

a = []
for i in range(n):
    a += board[i].split("#")

for j in range(m):
    tmp = ""
    for i in range(n):
        tmp += board[i][j]
    a += tmp.split("#")

b = []
for x in a:
    if x == "":
        continue
    if len(x) >= 2:
        b.append(x)
b.sort()
print(b[0])