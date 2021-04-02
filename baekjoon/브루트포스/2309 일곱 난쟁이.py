import sys
n = 9
a = [int(input()) for _ in range(n)]
a.sort()
total = sum(a)

for i in range(n):
    for j in range(i + 1, n):
        if total - a[i] - a[j] == 100:
            for k in range(n):
                if i != k and j != k:
                    print(a[k])
            sys.exit(0)