n = int(input())
h = [int(input()) for _ in range(n)]
stack = []
ans = 0

for x in h:
    while stack and stack[-1] <= x:
        stack.pop()
    stack.append(x)
    ans += len(stack) - 1

print(ans)
