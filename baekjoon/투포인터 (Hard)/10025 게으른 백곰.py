import sys
from collections import defaultdict

n, k = map(int, input().split())
ice = defaultdict(int)
min_l, max_l = sys.maxsize, 0
for _ in range(n):
    g, x = map(int, input().split())
    min_l = min(min_l, x)
    max_l = max(max_l, x)
    ice[x] = g

# now: 현재 얼음의 양
rt, now = min_l, 0
ans = -1
for lt in range(min_l, max_l + 1):
    while rt < max_l +1 and rt - lt <= 2 * k:
        if ice[rt] == 0:
            rt += 1
            continue
        now += ice[rt]
        rt += 1
    ans = max(ans, now)
    now -= ice[lt]
print(ans)