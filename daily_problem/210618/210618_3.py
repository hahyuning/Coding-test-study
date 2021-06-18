from collections import deque

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    q = deque()
    dist = dict()
    dist[a] = ""
    q.append((a, ""))

    while q:
        now, op = q.popleft()
        if now == b:
            print(op)
            break
        # 두 배
        if (2 * now) % 10000 not in dist:
            q.append(((2 * now) % 10000, op + "D"))
            dist[(2 * now) % 10000] = op + "D"
        # -1
        if (now + 9999) % 10000 not in dist:
            q.append(((now + 9999) % 10000, op + "S"))
            dist[(now + 9999) % 10000] = op + "S"
        # 오른쪽 회전
        now = str(now)
        k = 4 - len(now)
        now = "0" * k + now
        nxt = int(now[1:] + now[0])
        if nxt not in dist:
            q.append((nxt, op + "L"))
            dist[nxt] = op + "L"
        # 왼쪽 회전
        nxt = int(now[-1] + now[:-1])
        if nxt not in dist:
            q.append((nxt, op + "R"))
            dist[nxt] = op + "R"