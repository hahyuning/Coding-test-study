from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())

    # 어떤 수로부터 만들어 졌는지 저장
    fro = [-1] * n
    # 0과 1중 어떤 수를 더해서 만들어졌는지 저장
    how = [-1] * n
    how[1 % n] = 1

    dist = [-1] * n
    q = deque()
    q.append(1 % n)
    dist[1 % n] = 0

    while q:
        now = q.popleft()
        for i in [0, 1]:
            nxt = (now * 10 + i) % n
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1

                fro[nxt] = now
                how[nxt] = i
                q.append(nxt)

    if dist[0] == -1:
        print("BRAK")
    else:
        ans = ""
        i = 0
        while i != -1:
            ans += str(how[i])
            i = fro[i]
        print(ans[::-1])