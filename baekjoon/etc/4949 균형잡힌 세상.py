import sys

table = {")":"(", "]":"["}
valid_char = [")", "(", "]", "["]

while True:
    s = sys.stdin.readline().rstrip()

    if len(s) == 1:
        break

    stack = []
    check = -1

    for i, char in enumerate(s):

        if char in valid_char and char not in table:
            stack.append(char)
        elif char in valid_char and char in table:
            if not stack or stack.pop() != table[char]:
                print("no")
                break
        check = i

    if check == len(s) - 1 and len(stack) == 0:
        print("yes")
    elif check == len(s) - 1 and len(stack) != 0:
        print("no")