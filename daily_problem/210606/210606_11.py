import math

def check(x):
    res = True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            res = False
            break
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0 or n == 1:
        print(2)
        continue

    while True:
        if check(n):
            print(n)
            break
        n += 1

