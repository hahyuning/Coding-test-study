from collections import deque

hanoi = []
for _ in range(3):
    tmp = input().split()
    n = int(tmp[0])
    if n > 0:
        hanoi.append(tmp[1])
    else:
        hanoi.append("")

# 만들어야 할 최종 상태 찾기
cnt = [0, 0, 0]
for i in range(3):
    for s in hanoi[i]:
        cnt[ord(s) - ord("A")] += 1

ans = ["", "", ""]
for i in range(3):
    for j in range(cnt[i]):
        ans[i] += chr(ord("A") + i)

# -----------------------------------------------
# 딕셔너리 사용 -> 정점은 튜플로 변환
dist = dict()
q = deque()
q.append(tuple(hanoi))
dist[tuple(hanoi)] = 0

while q:
    now = q.popleft()
    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            if len(now[i]) == 0:
                continue

            # i 번째에서 j 번째로 이동
            next = list(now[:])
            next[j] += now[i][-1]
            next[i] = next[i][:-1]
            next = tuple(next)

            if next not in dist:
                dist[next] = dist[now] + 1
                q.append(next)

print(dist[tuple(ans)])