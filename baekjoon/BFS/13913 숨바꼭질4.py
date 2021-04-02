from collections import deque
import sys
sys.setrecursionlimit(200000)

n, k = map(int, input().split())
time = [-1] * 200001
time[n] = 0
path = [-1] * 200001
path[n] = n

q = deque()
q.append(n)

while q:
    now = q.popleft()
    for next in [now + 1, now - 1, 2 * now]:
        if 0 <= next <= 200000 and time[next] == -1:
            time[next] = time[now] + 1
            path[next] = now
            q.append(next)

print(time[k])

def find_path(n, k):
    if n != k:
        find_path(n, path[k])
    print(k, end=" ")

find_path(n, k)