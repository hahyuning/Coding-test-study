from collections import defaultdict

n = int(input())
a = defaultdict(int)
for _ in range(n):
    x = input()
    a[x] += 1

for _ in range(n - 1):
    x = input()
    a[x] -= 1

for i, x in a.items():
    if x != 0:
        print(i)
