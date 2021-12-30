from collections import deque

def solution(places):
    answer = []

    cnt = 1
    for place in places:
        for i in range(5):
            for j in range(5):
                if len(answer) == cnt:
                    continue

                if place[i][j] == "P":
                    people_dist = bfs(i, j, place)

                    print(people_dist)
                    if people_dist and min(people_dist) <= 2:
                        answer.append(0)

        if len(answer) < cnt:
            answer.append(1)
        cnt += 1

    return answer

def bfs(x, y, board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    ans = []
    d = [[-1] * 5 for _ in range(5)]
    q = deque()
    q.append((x, y))
    d[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and d[nx][ny] == -1:
                if board[nx][ny] != "X":
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    if board[nx][ny] == "P":
                        ans.append(d[nx][ny])

    return ans

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])