t = int(input())
ans = 0
for _ in range(t):
    s = input()
    stack = []

    for x in s:
        if not stack:
            stack.append(x)
        else:
            if x == "A":
                if stack[-1] == "A":
                    stack.pop()
                else:
                    stack.append(x)
            else:
                if stack[-1] == "B":
                    stack.pop()
                else:
                    stack.append(x)

    if not stack:
        ans += 1
print(ans)
