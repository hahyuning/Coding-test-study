import sys
input = sys.stdin.readline

n = int(input())
queue = [0] * n
begin = end = 0

for _ in range(n):
    op, *x = input().split()

    if op == "push":
        queue[end] = int(x[0])
        end += 1
    elif op == "front":
        if begin == end:
            print(-1)
        else:
            print(queue[begin])
    elif op == "size":
        print(end - begin)
    elif op == "empty":
        if begin == end:
            print(1)
        else:
            print(0)
    elif op == "pop":
        if begin == end:
            print(-1)
        else:
            print(queue[begin])
            begin += 1
    elif op == "back":
        if begin == end:
            print(-1)
        else:
            print(queue[end - 1])