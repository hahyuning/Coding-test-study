n = int(input())
need = list(map(int, input().split()))
foods = dict()
for i in range(n):
    foods[i] = list(map(int, input().split()))

ans = -1
ans_num = []
for i in range(1, 1 << n):
    res = []
    for k in range(n):
        if (i & (1 << k)) > 0:
            res.append(k)

    p, f, s, v, c = 0, 0, 0, 0, 0
    for x in res:
        p += foods[x][0]
        f += foods[x][1]
        s += foods[x][2]
        v += foods[x][3]
        c += foods[x][4]

    if p >= need[0] and f >= need[1] and s >= need[2] and v >= need[3]:
        if ans == -1 or c <= ans:
            ans = c
            ans_num.append([c] + res)

print(ans)
if ans != -1:
    ans_num.sort()
    tmp = ans_num[0][1:]
    for x in tmp:
        print(x + 1, end=" ")