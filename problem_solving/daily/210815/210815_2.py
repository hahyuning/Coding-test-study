n = int(input())
a = []
for _ in range(n):
    s, e = map(int, input().split())
    a.append((s, e))

a.sort(key=lambda x:(x[0], -(x[1] - x[0] + 1)))

calendar = [[0] * 366 for _ in range(n)]
for s, e in a:
    for i in range(n):
        if 1 in calendar[i][s:e + 1]:
            continue

        for j in range(s, e + 1):
            calendar[i][j] = 1
        break

# 칼럼별로 확인
h = 0
w = 0
ans = 0
for j in range(1, 366):
    check = False
    for i in range(n):
        if calendar[i][j] == 1:
            check = True
            h = max(h, i + 1)
    if check:
        w += 1
    else:
        ans += w * h
        h = 0
        w = 0
ans += w * h
print(ans)