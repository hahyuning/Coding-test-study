n, k = map(int, input().split())
# 내구도 리스트
a = list(map(int, input().split()))
# 로봇이 올라와 있는지 여부 체크
robot = [False] * (2 * n)

zero_cnt = 0
answer = 0

while True:
    # 회전 시작
    answer += 1
    a = a[-1:] + a[:-1]
    robot = robot[-1:] + robot[:-1]

    # 로봇이 내려가는 위치에 있으면 내리기
    # 아래 줄 (n ~ 2 * n - 1)에는 로봇 X
    if robot[n - 1]:
        robot[n - 1] = False
    # 로봇 이동
    for i in range(n - 2, -1, -1):
        if robot[i]:
            if robot[i + 1] == False and a[i + 1] > 0:
                robot[i + 1] = True
                robot[i] = False
                a[i + 1] -= 1
                if a[i + 1] == 0:
                    zero_cnt += 1

    # 로봇이 내려가는 위치에 있으면 내리기
    if robot[n - 1]:
        robot[n - 1] = False
    # 로봇이 올라가는 자리의 내구도가 0이 아니면 올리기
    if a[0] > 0:
        robot[0] = True
        a[0] -= 1
        if a[0] == 0:
            zero_cnt += 1
    if zero_cnt >= k:
        print(answer)
        break