from collections import deque

m, n = map(int, input().split())
ans = deque()
now = ""
for _ in range(n):
   x, k = input().split()
   k = int(k)
   l = len(now)

   if l + k < m:
      now += x * k
   else:
      nxt = x * (k - m + l)
      now += x * (m - l)
      ans.append(now)
      now = nxt

ans.appendleft(now)
for row in ans:
   print(row)