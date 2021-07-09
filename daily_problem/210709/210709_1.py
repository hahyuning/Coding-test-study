prime_num = [False] * 10001
prime_num[0] = prime_num[1] = True
p = []

for i in range(2, 10001):
    if not prime_num[i]:
        p.append(i)
        j = i * 2
        while j <= 10000:
            prime_num[j] = True
            j += i

t = int(input())
for _ in range(t):
    n = int(input())

    a = 0
    b = 0
    for x in p:
        if x > n // 2:
            break
        if not prime_num[n - x]:
            a = x
            b = n - x

    print("{0} {1}".format(a, b))
