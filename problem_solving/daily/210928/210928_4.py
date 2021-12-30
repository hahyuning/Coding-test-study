from collections import deque

def move(s):
    s = list(s)
    idx = s.index("0")
    res = []
    if idx + 3 <= 8:
        s[idx], s[idx + 3] = s[idx + 3], s[idx]
        res.append("".join(s))
        s[idx], s[idx + 3] = s[idx + 3], s[idx]
    if idx - 3 >= 0:
        s[idx], s[idx - 3] = s[idx - 3], s[idx]
        res.append("".join(s))
        s[idx], s[idx - 3] = s[idx - 3], s[idx]
    if idx + 1 <= 8 and (idx + 1) % 3 != 0:
        s[idx], s[idx + 1] = s[idx + 1], s[idx]
        res.append("".join(s))
        s[idx], s[idx + 1] = s[idx + 1], s[idx]
    if idx - 1 >= 0 and idx % 3 != 0:
        s[idx], s[idx - 1] = s[idx - 1], s[idx]
        res.append("".join(s))
        s[idx], s[idx - 1] = s[idx - 1], s[idx]
    return res

a = [list(map(int, input().split())) for _ in range(3)]
start = ""
for x in a:
    start += "".join(map(str, x))

dist = dict()
q = deque()
q.append(start)
dist[start] = 0

ans = -1
while q:
    now = q.popleft()
    if now == "123456780":
        ans = dist[now]
        break

    nxt_list = move(now)
    for nxt in nxt_list:
        if nxt not in dist:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

print(ans)
