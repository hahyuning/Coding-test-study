import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    a = [input().rstrip() for _ in range(n)]
    b = dict()
    for x in a:
        tmp = ""
        for i in range(len(x)):
            if x[i].isupper():
                tmp += x[i].lower()
            else:
                tmp += x[i]
        b[tmp] = x

    c = sorted(b.items(), key=lambda x:x[0])
    print(c[0][1])