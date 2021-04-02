def solution(n):
    answer = [[0] * n for _ in range(n)]

    ret = []
    x, y = -1, 0
    num = 1

    for i in range(n):
        for _ in range(i, n):
            # 아래
            if i % 3 == 0:
                x += 1
            # 오른쪽
            elif i % 3 == 1:
                y += 1
            # 왼쪽위 대각선
            else:
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1

    for x in answer:
        for j in x:
            if j != 0:
                ret.append(j)
    return ret

solution(3)