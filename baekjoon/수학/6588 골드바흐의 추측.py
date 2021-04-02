prime_num = [False] * 1000001
prime_num[0] = prime_num[1] = True
p = []

for i in range(2, 1000001):
    if not prime_num[i]:
        p.append(i)
        j = i * 2
        while j <= 1000000:
            prime_num[j] = True
            j += i

p = p[1:]

while True:
    n = int(input())
    if n == 0:
        break

    for x in p:
        if not prime_num[n - x]:
            print("{0} = {1} + {2}".format(n, x, n-x))
            break