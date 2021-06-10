import sys

def recursion(a, s):
    global min_val, max_val

    if len(a) == 1:
        if int(a[0]) % 2 == 1:
            s += 1

        if min_val == -1 or min_val > s:
            min_val = s
        if max_val == -1 or max_val < s:
            max_val = s
        return

    if len(a) == 2:
        for x in a:
            if int(x) % 2 == 1:
                s += 1
        recursion(str(int(a[0]) + int(a[1])), s)

    else:
        n = len(a)
        for x in a:
            if int(x) % 2 == 1:
                s += 1
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                b = int("".join(a[:i + 1])) + int("".join(a[i + 1:j + 1])) + int("".join(a[j + 1:]))
                recursion(str(b), s)

max_val = -1
min_val = -1
a = input()
recursion(a, 0)
print(min_val, max_val)
