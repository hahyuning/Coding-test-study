from collections import deque

n, k = map(int, input().split())
q = deque()
q.append(n)

visited = [[False] * 2 for _ in range(500001)]
visited[n][0] = True
level = 0
odd_even = 0

ans = -1
while q:
    # 동생이 50만보다 큰 좌표에 있는 경우
    if k > 500000:
        break
    # 수빈이가 이전에 방문한 곳을 동생이 방문한 경우
    if visited[k][odd_even]:
        ans = level
        break

    nxt_q = []
    odd_even = 1 - odd_even
    for now in q:
        for nxt in [now - 1, now + 1, 2 * now]:
            if 0 <= nxt <= 500000 and not visited[nxt][odd_even]:
                visited[nxt][odd_even] = True
                nxt_q.append(nxt)

    level += 1
    k += level
    q = nxt_q

print(ans)
