from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
b = a[::]
a = list(set(a))
a.sort()

for x in b:
    print(bisect_left(a, x), end=" ")