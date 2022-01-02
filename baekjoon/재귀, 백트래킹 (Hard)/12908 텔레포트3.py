def cal(a, b, c, d):
    return abs(a - c) + abs(b - d)

def solution(a, b, c, d, route):
    ans = cal(a, b, c, d)

    for i in range(len(route)):
        tmp = []
        for j in range(len(route)):
            if i != j:
                tmp.append((route[j][0], route[j][1], route[j][2], route[j][3]))

        d1 = cal(a, b, route[i][0], route[i][1]) + 10 + solution(route[i][2], route[i][3], c, d, tmp)
        d2 = cal(a, b, route[i][2], route[i][3]) + 10 + solution(route[i][0], route[i][1], c, d, tmp)
        ans = min(ans, d1, d2)

    return ans

sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
t = []
for _ in range(3):
    a, b, c, d = map(int, input().split())
    t.append((a, b, c, d))

print(solution(sx, sy, ex, ey, t))