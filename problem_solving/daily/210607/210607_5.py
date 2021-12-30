import math

n, m = map(int, input().split())

if n == m:
    print(0)
else:
    diff = int(math.sqrt(m - n))
    if diff ** 2 == m - n:
        print(2 * diff - 1)
    elif m - n <= diff ** 2 + diff:
        print(2 * diff)
    else:
        print(2 * diff + 1)
