from itertools import combinations
def game(n):
    global res
    # 종료 조건: 6개의 팀이 경기를 다 한 경우 (15가지)
    if n == 15:
        if sum(win) == 0 and sum(draw) == 0 and sum(lose) == 0:
            res = 1
        return

    a, b = tournament[n]
    # a가 이기고 b가 진경우
    if win[a] > 0 and lose[b] > 0:
        win[a] = win[a] - 1
        lose[b] = lose[b] - 1
        game(n + 1)
        win[a] = win[a] + 1
        lose[b] = lose[b] + 1
    # b가 이기고 a가 진경우
    if win[b] > 0 and lose[a] > 0:
        win[b] = win[b] - 1
        lose[a] = lose[a] - 1
        game(n + 1)
        win[b] = win[b] + 1
        lose[a] = lose[a] + 1
    # 비긴 경우
    if draw[a] > 0 and draw[b] > 0:
        draw[a] = draw[a] - 1
        draw[b] = draw[b] - 1
        game(n + 1)
        draw[a] = draw[a] + 1
        draw[b] = draw[b] + 1

tournament = list(combinations([0, 1, 2, 3, 4, 5], 2))
ans = []
for _ in range(4):
    a = list(map(int, input().split()))
    win, draw, lose = [], [], []
    for i in range(len(a)):
        if i % 3 == 0:
            win.append(a[i])
        elif i % 3 == 1:
            draw.append(a[i])
        else:
            lose.append(a[i])
    res = 0
    game(0)
    ans.append(res)

print(" ".join(map(str, ans)))