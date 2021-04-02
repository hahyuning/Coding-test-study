t = int(input())
# 0: n극, 1: s극
a = [list(map(int, input())) for _ in range(t)]
k = int(input())

for _ in range(k):
    # 1: 시계 방향, -1: 반시계 방향
    tobni, direction = map(int, input().split())
    tobni -= 1
    # 회전 여부 체크
    check = [0] * t
    check[tobni] = direction

    # 왼쪽 톱니 확인
    for i in range(tobni - 1, -1, -1):
        if a[i][2] != a[i + 1][6]:
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

answer = 0
for i in range(t):
    if a[i][0] == 1:
        answer += 1
print(answer)