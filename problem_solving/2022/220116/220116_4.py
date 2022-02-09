import re

p = re.compile('(100+1+|01)+')
t = int(input())
for _ in range(t):
    s = input()
    if p.fullmatch(s):
        print("YES")
    else:
        print("NO")