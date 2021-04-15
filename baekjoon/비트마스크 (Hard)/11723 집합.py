import sys
n = 20
m = int(sys.stdin.readline())
s = 0 # 집합

for _ in range(m):
    op, *num = sys.stdin.readline().split()
    if len(num) > 0:
        x = int(num[0]) - 1

    if op == "add":
        s = (s | (1 << x))
    elif op == "remove":
        s = (s & ~(1 << x))
    elif op == "check":
        res = (s & (1 << x))
        if res > 0:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")

    elif op == "toggle":
        s = (s ^ (1 << x))
    elif op == "all":
        s = (1 << n) - 1
    else:
        s = 0

