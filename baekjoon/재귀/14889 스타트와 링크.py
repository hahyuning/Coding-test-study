n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
#------------------------------------------------------------
# 비트마스크
ans = -1

for i in range((1 << n)):
    first = []
    second = []
    for j in range(n):
        if (i & (1 << j)) > 0:
            first += [j]
        else:
            second += [j]
    if len(first) != n // 2:
        continue

    t1 = 0
    t2 = 0
    for l1 in range(n // 2):
        for l2 in range(n // 2):
            if l1 == l2:
                continue
            t1 += s[first[l1]][first[l2]]
            t2 += s[second[l1]][second[l2]]

    diff = abs(t1 - t2)
    if ans == -1 or ans > diff:
        ans = diff
print(ans)

#----------------------------------------------------------
# 조합
def calculation(start, link):
    if len(start) != n // 2:
        return -1
    if len(link) != n // 2:
        return -1
    t1 = 0
    t2 = 0
    for i in range(n // 2):
        for j in range(n // 2):
            if i == j:
                continue
            t1 += s[start[i]][start[j]]
            t2 += s[link[i]][link[j]]
    diff = abs(t1 - t2)
    return diff

ans = 1000
def combination(index, start, link):
    global ans

    if index == n:
        tmp = calculation(start, link)
        if tmp != -1:
            ans = min(ans, tmp)
        return

    combination(index + 1, start + [index], link)
    combination(index + 1, start, link + [index])

combination(0, [], [])
print(ans)