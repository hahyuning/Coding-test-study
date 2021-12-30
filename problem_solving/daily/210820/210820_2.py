import sys

def solution(idx, x):
    global ans

    if idx == len(op):
        ans = max(ans, int(x))
        return

    y = str(eval(x + op[idx] + num[idx + 1]))
    solution(idx + 1, y)

    if idx + 1 < len(op):
        y = str(eval(num[idx + 1] + op[idx + 1] + num[idx + 2]))
        y = str(eval(x + op[idx] + y))
        solution(idx + 2, y)

n = int(input())
s = input()
num = []
op = []
for x in s:
    if x != "+" and x != "-" and x != "*":
        num.append(x)
    else:
        op.append(x)

ans = -sys.maxsize
solution(0, num[0])
print(ans)