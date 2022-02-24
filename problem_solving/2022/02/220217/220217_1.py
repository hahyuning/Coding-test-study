import sys
input = sys.stdin.readline


n = int(input())
m = int(input())

bus = []
for i in range(1, m + 1):
    a, b = map(int, input().split())

    if a < b:
        bus.append((a, b, i))
        bus.append((a + n, b + n, i))
    else:
        bus.append((a, b + n, i))

bus.sort(key=lambda x: (x[0], -x[1]))
deleted = dict()
rt = 0

for s, e, num in bus:
    if e <= rt:
        deleted[num] = True
    else:
        rt = e

for i in range(1, m + 1):
    if i not in deleted:
        print(i, end=" ")