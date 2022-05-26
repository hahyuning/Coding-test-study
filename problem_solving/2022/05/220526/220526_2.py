from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))
f = defaultdict(int)

for x in a:
    f[x] += 1

ans = [-1] * n
stack = []
for i in range(n):
    if not stack:
        stack.append((f[a[i]], i))
    else:
        while stack and stack[-1][0] < f[a[i]]:
            x, j = stack.pop()
            ans[j] = a[i]
        stack.append((f[a[i]], i))

print(*ans)