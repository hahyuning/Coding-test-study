def solution(i, a, b, x):
    global ans

    if i == n:
        if x == k:
            return True
        else:
            return False

    # 메모이제이션: 정답을 찾으면 정답을 출력하고 종료
    if d[i][a][b][x]:
        return False

    d[i][a][b][x] = True

    tmp = ans
    ans = tmp + "A"
    if solution(i + 1, a + 1, b, x):
        return True
    ans = tmp + "B"
    if solution(i + 1, a, b + 1, x + a):
        return True
    ans = tmp + "C"
    if solution(i + 1, a, b, x + a + b):
        return True

    return False

n, k = map(int, input().split())
# d[i][a][b][x]: 길이가 i이고, A의 개수가 a개, B의 개수가 b개, 조건을 만족하는 쌍이 x개
# 초기상태: d[0][0][0][0] = 1
d = [[[[False] * ((30 * 29) // 2 + 1) for _ in range(31)] for _ in range(31)] for _ in range(31)]

ans = ""
if solution(0, 0, 0, 0):
    print(ans)
else:
    print(-1)