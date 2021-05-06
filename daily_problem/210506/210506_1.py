import sys

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]

cnt = 0
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            cnt += 1
            for k in range(3):
                for l in range(3):
                    a[i + k][j + l] = 1 - a[i + k][j + l]

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            print(-1)
            sys.exit(0)

print(cnt)


