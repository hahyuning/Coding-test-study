from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
company = defaultdict(int)

for _ in range(n):
    name, state = input().split()
    if state == "enter":
        company[name] += 1
    else:
        company[name] -= 1

ans = []
for k, v in company.items():
    if v > 0:
        ans.append(k)

ans.sort(reverse=True)
for n in ans:
    print(n)