def solution(a, b, c, x1, x2):
    if a + b + c == n:
        d[a][b][c][x1][x2] = 1
        return d[a][b][c][x1][x2]

    if d[a][b][c][x1][x2] != -1:
        return d[a][b][c][x1][x2]

    if a + 1 <= cnt[0]:
        if solution(a + 1, b, c, 0, x1) == 1:
            d[a][b][c][x1][x2] = 1
            return d[a][b][c][x1][x2]

    if b + 1 <= cnt[1] and x1 != 1:
        if solution(a, b + 1, c, 1, x1) == 1:
            d[a][b][c][x1][x2] = 1
            return d[a][b][c][x1][x2]

    if c + 1 <= cnt[2] and x1 != 2 and x2 != 2:
        if solution(a, b, c + 1, 2, x1) == 1:
            d[a][b][c][x1][x2] = 1
            return d[a][b][c][x1][x2]

    d[a][b][c][x1][x2] = 0
    return d[a][b][c][x1][x2]

def path(a, b, c, x1, x2):
    if a + b + c == n:
        return ""

    if a + 1 <= cnt[0] and solution(a + 1, b, c, 0, x1) == 1:
        return "A" + path(a + 1, b, c, 0, x1)

    if b + 1 <= cnt[1] and x1 != 1 and solution(a, b + 1, c, 1, x1) == 1:
        return "B" + path(a, b + 1, c, 1, x1)

    if c + 1 <= cnt[2] and x1 != 2 and x2 != 2 and solution(a, b, c + 1, 2, x1) == 1:
        return "C" + path(a, b, c + 1, 2, x1)

    return ""

s = input()
cnt = [0, 0, 0]
n = len(s)
for x in s:
    cnt[ord(x) - ord("A")] += 1

# d[a][b][c][x1][x2]: A, B, C의 개수가 a, b, c이고 전날 일한 사람이 x1, 이틀전에 일한 사람이 x2
d = [[[[[-1] * 3 for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]
res = solution(0, 0, 0, 0, 0)
if res == 0:
    print(-1)
else:
    print(path(0, 0, 0, 0, 0))