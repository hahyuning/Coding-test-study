from collections import defaultdict
n = int(input())
file = defaultdict(int)
for _ in range(n):
    a, b = input().split(".")
    file[b] += 1

ans = []
for x, cnt in file.items():
    ans.append((x, cnt))
ans.sort(key=lambda x:x[0])
for a, b in ans:
    print(a, end=" ")
    print(b)