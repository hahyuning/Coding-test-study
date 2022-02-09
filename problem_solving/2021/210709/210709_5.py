prime_num = [False] * 100001
prime_num[0] = prime_num[1] = True

for i in range(2, 100001):
    if not prime_num[i]:
        j = i * 2
        while j <= 100000:
            prime_num[j] = True
            j += i

t = int(input())
for _ in range(t):
    n = int(input())

    for i in range(2, 100001):
        if prime_num[i]:
            continue

        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt != 0:
            print(i, cnt)
        if n == 1:
            break
