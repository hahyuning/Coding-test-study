import sys
input=sys.stdin.readline

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def empty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return -1

    def size(self):
        return len(self.stack)

    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return -1

if __name__ == '__main__':
    n = int(input())
    stack = Stack()

    for _ in range(n):
        s = input().split()
        operation = s[0]
        if operation == "push":
            stack.push(int(s[1]))
        elif operation == "pop":
            print(stack.pop())
        elif operation == "size":
            print(stack.size())
        elif operation == "empty":
            print(stack.empty())
        else:
            print(stack.top())
