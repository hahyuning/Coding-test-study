prime = [False] * 10001
prime[1] = True

for i in range(2, 10001):
    if prime[i] == False:
        for j in range(2 * i, 10001, i):
            prime[j] = True

n = int(input())
m = int(input())

min_prime = -1
sum_prime = 0
for x in range(n, m + 1):
    if prime[x] == False:
        if min_prime == -1:
            min_prime = x
        sum_prime += x

if min_prime == -1:
    print(-1)
else:
    print(sum_prime)
    print(min_prime)
