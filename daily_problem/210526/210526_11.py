n = int(input())
s = input()
num = dict()
for i in range(n):
    num[chr(65 + i)] = int(input())

a = []
for x in s:
    if x in ["*", "-", "+", "/"]:
        a.append(x)
    else:
        a.append(num[x])

stack = []
for x in a:
    if x in ["*", "-", "+", "/"]:
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(format(eval(str(num2) + x + str(num1)), ".2f"))
    else:
        stack.append(x)

print(format(float(stack[0]), ".2f"))
