from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
wait = defaultdict(int)
cnt = 1
for _ in range(m):
    x = input().rstrip()
    wait[x] = cnt
    cnt += 1

ans = sorted(wait.items(), key=lambda x:x[1])
i = 0
while i < len(ans) and i < n:
    print(ans[i][0])
    i += 1