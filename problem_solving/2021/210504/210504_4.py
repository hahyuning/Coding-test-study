from collections import deque

t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    bipart = [[] for _ in range(2)]
    check = [False] * (v + 1)

    q = deque()
    q.append((1, 0))
    check[1] = True
    bipart[0].append(1)

    flg = True
    while q:
        now, s = q.popleft()
        for nxt in graph[now]:
            # 같은 집합 안에 있으면 종료
            if nxt in bipart[s]:
                flg = False
                break

            if nxt not in bipart[1 - s] and check[nxt] == False:
                bipart[1 - s].append(nxt)
                q.append((nxt, 1 - s))
                check[nxt] = True

        if flg == False:
            break

        # 그래프가 분리되있는 경우
        if not q:
            for i in range(1, v + 1):
                if check[i] == False:
                    bipart[0].append(i)
                    q.append((i, 0))
                    check[i] = True
                    break

    if flg == False:
        print("NO")
    else:
        print("YES")