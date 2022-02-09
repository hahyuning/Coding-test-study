r, c, w = map(int, input().split())
c -= 1

pascal = [[0 for _ in range(r + w + 1)] for _ in range(r + w + 1)]
for i in range(1, r + w + 1):
    pascal[i][0] = 1
    pascal[i][i - 1] = 1

    for j in range(1, i - 1):
        pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

ans = 0
cnt = 1
for i in range(r, r + w):
    for j in range(c, c + cnt):
        ans += pascal[i][j]
    cnt += 1
print(ans)