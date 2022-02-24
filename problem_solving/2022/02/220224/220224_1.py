import sys
input = sys.stdin.readline

n, m = map(int, input().split())
picture = [list(input().rstrip()) for _ in range(n)]

min_cnt = n
ans = [["."] * m for _ in range(n)]
for j in range(m):
    cnt = -1
    tmp = []
    for i in range(n):
        if picture[i][j] == "X":
            cnt = 0
        elif picture[i][j] == "#":
            ans[i][j] = "#"
            if cnt != -1:
                min_cnt = min(min_cnt, cnt)
        else:
            if cnt != -1:
                cnt += 1


for j in range(m):
    for i in range(n):
        if picture[i][j] == "X":
            ans[i + min_cnt][j] = picture[i][j]
            picture[i][j] = "."

for row in ans:
    print("".join(row))
