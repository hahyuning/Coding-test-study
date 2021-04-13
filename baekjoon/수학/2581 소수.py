import math
m = int(input())
n = int(input())

def prime_number(x):
    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

sum = 0
first = 0

for i in range(m, n + 1):
    if prime_number(i):
        if first == 0:
            first = i
        sum += i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(first)