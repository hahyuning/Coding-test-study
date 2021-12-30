x = []
while True:
    try:
        a, b = map(int, input().split())
        x.append((a, b))
    except:
        break

d = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(len(x) + 1)]

# i번째 선수에 대해, i번째 선수가 백팀으로 출전하는 경우, 흑팀으로 출전하는 경우, 출전하지 않는 경우 계산
for i in range(len(x)):
    for w in range(16):
        for b in range(16):
            if w + 1 <= 15:
                d[i + 1][w + 1][b] = max(d[i + 1][w + 1][b], d[i][w][b] + x[i][0])
            if b + 1 <= 15:
                d[i + 1][w][b + 1] = max(d[i + 1][w][b + 1], d[i][w][b] + x[i][1])

            # 출전하지 않는 경우
            d[i + 1][w][b] = max(d[i + 1][w][b], d[i][w][b])

print(d[len(x)][15][15])
