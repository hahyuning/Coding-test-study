n = int(input())
a = list(map(int, input().split()))

stack = []
ans = [-1] * n
for i in range(n):
    if not stack:
        stack.append((a[i], i))
    else:
        while stack and stack[-1][0] < a[i]:
            x, j = stack.pop()
            ans[j] = a[i]
        stack.append((a[i], i))

print(*ans)