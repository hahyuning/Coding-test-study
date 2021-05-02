n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

# 풀이 1. 비트마스크
ans = -1
for i in range((1 << n)):
    first = []
    second = []
    for j in range(n):
        if (i & (1 << j)) > 0:
            first += [j]
        else:
            second += [j]
    # 팀이 반반으로 나누어지지 않은 경우
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


# 풀이 2. 조합
def calculation(start, link):
    # 백트래킹
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

def combination(index, start, link):
    global ans
    # 종료 조건: 인덱스가 끝에 도달한 경우
    if index == n:
        # 각 팀의 점수 계산
        tmp = calculation(start, link)
        if tmp != -1:
            ans = min(ans, tmp)
        return

    combination(index + 1, start + [index], link)
    combination(index + 1, start, link + [index])

ans = 1000
combination(0, [], [])
print(ans)