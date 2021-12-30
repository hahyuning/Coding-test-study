s = input()
b = input()
n = len(b)
stack = []

for char in s:
    if char != b[-1]:
        stack.append(char)

    else:
        imsi = []
        imsi.append(char)
        i = -2
        while stack and i >= -n and stack[-1] == b[i]:
            a = stack.pop()
            imsi.append(a)
            i -= 1

        if len(imsi) != n:
            while imsi:
                stack.append(imsi.pop())

if len(stack) != 0:
    print("".join(stack))
else:
    print("FRULA")
