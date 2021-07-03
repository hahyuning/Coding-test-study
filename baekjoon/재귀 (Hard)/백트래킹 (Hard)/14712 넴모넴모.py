def solution(cnt):
    global ans
    if cnt == n * m:
        ans += 1
        return

    # 일차원 좌표를 이차원 좌표로 변환
    x = cnt // m + 1
    y = cnt % m + 1

    # 네모를 놓지 않는 경우
    solution(cnt +  1)
    # 네모를 놓는 경우
    if not board[x - 1][y] or not board[x][y - 1] or not board[x - 1][y - 1]:
        board[x][y] = True
        solution(cnt + 1)
        board[x][y] = False

n, m = map(int, input().split())
board = [[False] * (m + 1) for _ in range(n + 1)]
ans = 0
solution(0)
print(ans)