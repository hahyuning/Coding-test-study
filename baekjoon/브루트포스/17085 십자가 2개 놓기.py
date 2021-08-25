n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]

ans = 0
for x1 in range(n):
    for y1 in range(m):
        s1 = 0
        while True:
            if x1 - s1 < 0 or x1 + s1 >= n or y1 - s1 < 0 or y1 + s1 >= m:
                break

            if a[x1 - s1][y1] != "#" or a[x1 + s1][y1] != "#" or a[x1][y1 - s1] != "#" or a[x1][y1 + s1] != "#":
                break

            a[x1 - s1][y1] = a[x1 + s1][y1] = a[x1][y1 - s1] =  a[x1][y1 + s1] = "*"

            for x2 in range(n):
                for y2 in range(m):
                    s2 = 0
                    while True:
                        if x2 - s2 < 0 or x2 + s2 >= n or y2 - s2 < 0 or y2 + s2 >= m:
                            break

                        if a[x2 - s2][y2] != "#" or a[x2 + s2][y2] != "#" or a[x2][y2 - s2] != "#" or a[x2][y2 + s2] != "#":
                            break

                        ans = max(ans, (4 * s1 + 1) * (4 * s2 + 1))
                        s2 += 1

            s1 += 1

        s1 = 0
        while True:
            if x1 - s1 < 0 or x1 + s1 >= n or y1 - s1 < 0 or y1 + s1 >= m:
                break

            if a[x1 - s1][y1] != "*" or a[x1 + s1][y1] != "*" or a[x1][y1 - s1] != "*" or a[x1][y1 + s1] != "*":
                break

            a[x1 - s1][y1] = a[x1 + s1][y1] = a[x1][y1 - s1] = a[x1][y1 + s1] = "#"

            s1 += 1

print(ans)