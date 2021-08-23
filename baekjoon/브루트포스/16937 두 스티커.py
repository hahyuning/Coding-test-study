h, w = map(int, input().split())
n = int(input())
a = []
for _ in range(n):
    r, c = map(int, input().split())
    a.append((r, c))

ans = 0
for i in range(n):
    r1, c1 = a[i][0], a[i][1]
    for j in range(i, n):
        if i == j:
            continue
        r2, c2 = a[j][0], a[j][1]

        # 회전
        for x in range(2):
            for y in range(2):
                # 세로로 붙이는 경우
                if r1 + r2 <= h and max(c1, c2) <= w:
                    tmp = r1 * c1 + r2 * c2
                    ans = max(ans, tmp)

                # 가로로 붙이는 경우
                if max(r1, r2) <= h and c1 + c2 <= w:
                    tmp = r1 * c1 + r2 * c2
                    ans = max(ans, tmp)

                r2, c2 = c2, r2
            r1, c1 = c1, r1

print(ans)
