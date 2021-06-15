import re

s = input()
p = re.compile("(100+1+|01)+")
ans = p.fullmatch(s)
if ans:
    print("SUBMARINE")
else:
    print("NOISE")