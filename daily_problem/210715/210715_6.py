import sys

a = [int(input()) for _ in range(9)]
a.sort()
total = sum(a)

for i in range(9):
    for j in range(9):
        if i == j:
            continue

        if total - a[i] - a[j] == 100:
            for k, x in enumerate(a):
                if k != i and k != j:
                    print(x)
            sys.exit(0)