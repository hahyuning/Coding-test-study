import math

def prime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def dfs(m, num):
    if m == n:
        if prime(num):
            print(num)
        return

    if not prime(num):
        return

    for x in range(10):
        dfs(m + 1, int(str(num) + str(x)))

n = int(input())
for i in range(1, 10):
        dfs(1, i)