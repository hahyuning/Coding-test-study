import sys

def calculation(start, link):
    # 백트래킹
    if len(start) == 0:
        return -1
    if len(link) == 0:
        return -1

    t1 = 0
    t2 = 0
    for i in start:
        for j in start:
            if i == j:
                continue
            t1 += scores[i][j]

    for i in link:
        for j in link:
            if i == j:
                continue
            t2 += scores[i][j]

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

# --------------------------------------------------------
n = int(sys.stdin.readline())
scores = [list(map(int, input().split())) for _ in range(n)]

combination(0, [], [])
print(ans)