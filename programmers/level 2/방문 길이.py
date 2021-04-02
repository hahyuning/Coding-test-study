def solution(dirs):
    answer = 0
    move = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}
    visited = []
    x, y = 0, 0
    for dir in dirs:
        nx = x + move[dir][0]
        ny = y + move[dir][1]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        if (x, y, nx, ny) not in visited and (nx, ny, x, y) not in visited:
            answer += 1
            visited.append((x, y, nx, ny))
        x = nx
        y = ny
    return answer