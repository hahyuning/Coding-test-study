# 2. 게임 시뮬레이션
def simulate():
    # 현재 타자
    now = 0
    # 전체 점수
    score = 0
    for inning in range(n):
        # 1루, 2루, 3루
        b1, b2, b3 = 0, 0, 0
        # 아웃 횟수
        out = 0
        while out < 3:
            res = a[inning][player[now]]
            if res == 0:
                out += 1
            elif res == 1:
                score += b3
                b3, b2, b1 = b2, b1, 1
            elif res == 2:
                score += b3 + b2
                b3, b2, b1 = b1, 1, 0
            elif res == 3:
                score += b3 + b2 + b1
                b3, b2, b1 = 1, 0, 0
            elif res == 4:
                score += b3 + b2 + b1 + 1
                b3, b2, b1 = 0, 0, 0
            now += 1
            if now == 9:
                now = 0
    return score

# 1. 타순 결정
def order(index):
    if index == 9:
        return simulate()

    # 4번 타자는 1번 선수로 고정
    if index == 3:
        player[index] = 0
        return order(index + 1)

    ans = 0
    for i in range(1, 9):
        if check[i]:
            continue
        check[i] = True
        player[index] = i
        tmp = order(index + 1)
        check[i] = False
        player[index] = 0

        if ans < tmp:
            ans = tmp
    return ans

n = int(input())
# a[i][j]: i번째 이닝에 j번째 선수의 결과
a = [list(map(int, input().split())) for _ in range(n)]
# 각 선수의 순서를 기록할 리스트
player = [0] * 9
check = [False] * 9

print(order(0))
