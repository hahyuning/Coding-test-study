import re


n = int(input())
s = input()
idx = s.index("*")

pattern = s[:idx] + "[a-z]*" + s[idx + 1:]
p = re.compile(pattern)

for _ in range(n):
    t = input()
    if p.fullmatch(t):
        print("DA")
    else:
        print("NE")