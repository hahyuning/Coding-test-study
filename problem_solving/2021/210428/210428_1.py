dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = int(input())
for _ in range(t):
    order = input()
    path = set()
    path.add((0, 0))

    x = y = 0
    direction = 0
    for k in order:
        if k == "R":
            direction = (direction + 1) % 4
            continue
        if k == "L":
            direction = (direction + 3) % 4
            continue

        if k == "B":
            nx = x - dx[direction]
            ny = y - dy[direction]
            path.add((nx, ny))
            x = nx
            y = ny
            continue

        nx = x + dx[direction]
        ny = y + dy[direction]
        path.add((nx, ny))
        x = nx
        y = ny


    min_x = 1000
    max_x = -1000
    min_y = 1000
    max_y = -1000


    for a, b in path:
        min_x = min(min_x, a)
        max_x = max(max_x, a)
        min_y = min(min_y, b)
        max_y = max(max_y, b)

    print((max_y - min_y) * (max_x - min_x))