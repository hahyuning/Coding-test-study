t, w = map(int, input().split())
location = [0] + [int(input()) for _ in range(t)]
# d[i][j][k]: i번째 열매에 대해서 j번 움직였을때 먹을 수 있는 자두의 최대 개수 (k는 자두의 위치)
d = [[0] * (w + 1) for _ in range(t + 1)]

for i in range(1, t + 1):
    # 한번도 움직이지 않은 경우
    if location[i] == 1:
        d[i][0] = d[i - 1][0] + 1
    else:
        d[i][0] = d[i - 1][0]

    for j in range(1, w + 1):
        # 자두를 받아먹는 경우
        if location[i] == 1 and j % 2 == 0:
            d[i][j]= max(d[i - 1][j], d[i - 1][j - 1]) + 1
        elif location[i] == 2 and j % 2 == 1:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - 1]) + 1
        # 자두를 안먹는 경우
        else:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - 1])

print(max(d[t]))
