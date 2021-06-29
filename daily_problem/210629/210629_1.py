import sys
input = sys.stdin.readline
import re

p = re.compile("[A-F]?A+F+C+[A-F]?")
n =int(input())
for _ in range(n):
    s = input().rstrip()
    m = p.fullmatch(s)
    if m:
        print("Infected!")
    else:
        print("Good")