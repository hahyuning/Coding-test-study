import sys
input = sys.stdin.readline

n, m = map(int, input().split())
check = [[False] * m for _ in range(n)]

a = [input().rstrip() for _ in range(n)]
ans = []

for i in range(n):
    for j in range(m):
        if a[i][j] == "*":
            l = 0
            k = 1
            while True:
                if i - k >= 0 and i + k < n and j - k >= 0 and j + k < m:
                    if a[i + k][j] == "*" and a[i - k][j] == "*" and a[i][j - k] == "*" and a[i][j + k] == "*":
                        l = k
                    else:
                        break
                else:
                    break
                k += 1

            if l > 0:
                ans.append((i + 1, j + 1, l))
                check[i][j] = True
                for k in range(1, l + 1):
                    check[i + k][j] = True
                    check[i - k][j] = True
                    check[i][j + k] = True
                    check[i][j - k] = True

for i in range(n):
    for j in range(m):
        if a[i][j] == "*" and not check[i][j]:
            print(-1)
            sys.exit(0)

print(len(ans))
for x in ans:
    print(*x)

