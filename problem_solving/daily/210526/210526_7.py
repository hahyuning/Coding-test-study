from collections import defaultdict
n = int(input())
ans = 0
# 0 초기값, 1 왼쪽, 2 오른쪽
caw = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    if caw[a] == 0:
        caw[a] = b + 1
        continue

    if caw[a] != b + 1:
        ans += 1
        caw[a] = b + 1

print(ans)
