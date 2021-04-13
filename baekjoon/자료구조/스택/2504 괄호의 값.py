data = input()

def check(data):
    stack = []
    for s in data:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if not stack:
                return False
            if stack.pop() == "(":
                continue
            else:
                return False
        elif s == "]":
            if not stack:
                return False
            if stack.pop() == "[":
                continue
            else:
                return False
    if stack:
        return False
    else:
        return True

def calculate(data):
    stack = []
    for s in data:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if stack[-1] == "(":
                stack[-1] = 2
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == "(":
                        stack[-1] = tmp * 2
                        break
                    else:
                        tmp += stack.pop()
        elif s == "]":
            if stack[-1] == "[":
                stack[-1] = 3
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == "[":
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack.pop()
    return sum(stack)

if check(data):
    print(calculate(data))
else:
    print(0)