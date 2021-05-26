from collections import deque
n = int(input())
order = list(map(int, input().split()))
order.reverse()

i = 1
stack = deque()
for x in order:
    if x == 1:
        stack.append(i)
    elif x == 2:
        stack.insert(-1, i)
    else:
        stack.appendleft(i)
    i += 1

stack.reverse()
print(*stack)