s = input()

if s == "P" or s == "PPAP":
    print("PPAP")
else:
    stack = []
    for x in s:
        stack.append(x)

        if len(stack) >= 4:
            if "".join(stack[-4:]) == "PPAP":
                stack.pop()
                stack.pop()
                stack.pop()

    if "".join(stack) == "PPAP" or "".join(stack) == "P":
        print("PPAP")
    else:
        print("NP")

