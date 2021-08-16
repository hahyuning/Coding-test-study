from collections import deque

s = int(input())
dist = [[-1] * (s + 1) for _ in range(s + 1)]
dist[1][0] = 0

q = deque()
q.append((1, 0))

while q:
    screen, clipboard = q.popleft()
    # 클립보드로 복사
    if dist[screen][screen] == -1:
        dist[screen][screen] = dist[screen][clipboard] + 1
        q.append((screen, screen))
    # 화면에 붙여넣기
    if screen + clipboard <= s and dist[screen + clipboard][clipboard] == -1:
        dist[screen + clipboard][clipboard] = dist[screen][clipboard] + 1
        q.append((screen + clipboard, clipboard))
    # 한 개 삭제
    if 0 <= screen - 1 and dist[screen - 1][clipboard] == -1:
        dist[screen - 1][clipboard] = dist[screen][clipboard] + 1
        q.append((screen - 1, clipboard))

answer = s + 1
for x in dist[s]:
    if x != -1:
        answer = min(answer, x)
print(answer)


