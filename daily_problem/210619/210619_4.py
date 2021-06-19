# 톱니의 개수
t = 4
# 0: n극, 1: s극
a = [list(map(int, input())) for _ in range(t)]
# 회전 횟수
k = int(input())

for _ in range(k):
    # 1: 시계 방향, -1: 반시계 방향
    tobni, direction = map(int, input().split())
    tobni -= 1
    # 톱니의 회전 여부 체크
    check = [0] * t
    check[tobni] = direction

    # 왼쪽 톱니 확인
    for i in range(tobni - 1, -1, -1):
        # 맞닿은 극이 서로 다르면
        if a[i][2] != a[i + 1][6]:
            # 반대방향으로 회전
            check[i] = -check[i + 1]
        else:
            break
    # 오른쪽 톱니 확인
    for i in range(tobni + 1, t):
        if a[i - 1][2] != a[i][6]:
            check[i] = -check[i - 1]
        else:
            break

    # 회전 진행
    for i in range(t):
        if check[i] == 0:
            continue
        # 뒤로 한 칸씩 밀기
        if check[i] == 1:
            tmp = a[i][7]
            for j in range(7, 0, -1):
                a[i][j] = a[i][j - 1]
            a[i][0] = tmp
        # 앞으로 한 칸씩 땡기기
        else:
            tmp = a[i][0]
            for j in range(7):
                a[i][j] = a[i][j + 1]
            a[i][7] = tmp

# 12시 방향이 s극인 톱니바퀴의 개수 출력
answer = 0
for i in range(t):
    if a[i][0] == 1:
        answer += 2 ** i
print(answer)