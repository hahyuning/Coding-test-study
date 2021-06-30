from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))
lt, rt = 0, 0
ans = -1
q = deque()
cnt = 0
for lt in range(n):
    while rt < n and cnt < k:
        q.append(a[rt])
        if a[rt] == 1:
            cnt += 1
        rt += 1
    if cnt == k:
        if ans == -1 or len(q) < ans:
            ans = len(q)
        if a[lt] == 1:
            cnt -= 1
        lt += 1
        q.popleft()
print(ans)

