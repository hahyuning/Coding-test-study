from collections import deque

n = int(input())
a = list(map(int, input().split()))
s = int(input())
check = [False] * n

q = deque()
q.append(s - 1)
check[s - 1] = True

while q:
    now = q.popleft()
    for nxt in [now + a[now], now - a[now]]:
        if 0 <= nxt < n and not check[nxt]:
            q.append(nxt)
            check[nxt] = True

print(sum(check))