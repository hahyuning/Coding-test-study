n, m = map(int, input().split())
a = [[False] * (n + 1) for _ in range(n + 1)]
cnt = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    a[x][y] = True
    a[y][x] = True

    cnt[x] += 1
    cnt[y] += 1

ans = -1
for i in range(1, n - 1):
    for j in range(i + 1, n):
        # if문 먼저 안거르면 시간초과
        if a[i][j]:
            for k in range(j + 1, n + 1):
                if a[i][k] and a[j][k]:
                    tmp = cnt[i] + cnt[j] + cnt[k] - 6
                    if ans == -1 or tmp < ans:
                        ans = tmp
print(ans)



