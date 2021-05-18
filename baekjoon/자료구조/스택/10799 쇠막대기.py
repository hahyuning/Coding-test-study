s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    elif s[i] == ")":
        stack.pop()
        # 레이저인 경우
        if s[i - 1] == "(":
            cnt += len(stack)
        # 쇠막대기인 경우
        else:
            cnt += 1

print(cnt)