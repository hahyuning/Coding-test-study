n = int(input())
stack = []

ans = 0
for _ in range(n):
    x, y = map(int, input().split())

    while stack and stack[-1] > y:
        stack.pop()
        ans += 1

    if y == 0:
        continue

    if not stack or stack[-1] < y:
        stack.append(y)

while stack:
    stack.pop()
    ans += 1
print(ans)