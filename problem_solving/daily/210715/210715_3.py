import math

n, m = map(int, input().split())
a = [input() for _ in range(n)]

ans = -1
for x in range(n):
    for y in range(m):
        for dx in range(-n, n):
            for dy in range(-m, m):
                if dx == 0 and dy == 0:
                    continue

                tmp = ""
                nx = x
                ny = y

                while 0 <= nx < n and 0 <= ny < m:
                    tmp += a[nx][ny]

                    if int(math.sqrt(int(tmp))) ** 2 == int(tmp):
                        ans = max(ans, int(tmp))
                    nx += dx
                    ny += dy
print(ans)
