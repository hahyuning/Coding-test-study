n = int(input())
primes = [True] * 1004002
primes[1] = False
for i in range(2, 1004002):
    if primes[i]:
        for j in range(2 * i, 1004002, i):
            primes[j] = False

for i in range(n, 1004002):
    if primes[i]:
        x = str(i)
        if x == x[::-1]:
            print(i)
            break