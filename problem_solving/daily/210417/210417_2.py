# 올바른 괄호인지 체크하는 함수
def check(string):
    stack = []

    for s in string:
        if s == "(" or s == "[":
            stack.append(s)
            continue

        if s == ")":
            if not stack:
                return False
            t = stack.pop()
            if t != "(":
                return False
        elif s == "]":
            if not stack:
                return False
            t = stack.pop()
            if t != "[":
                return False

    if stack:
        return False
    return True

string = input()
if not check(string):
    print(0)
else:
    stack = []
    for s in string:
        if s == "(" or s == "[":
            stack.append(s)

        elif s == ")":
            if stack[-1] == "(":
                stack[-1] = 2
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[-1] == "(":
                        stack[-1] = tmp * 2
                        break
                    tmp += stack.pop()

        elif s == "]":
            if stack[-1] == "[":
                stack[-1] = 3
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[-1] == "[":
                        stack[-1] = tmp * 3
                        break
                    tmp += stack.pop()

    print(sum(stack))