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

t = int(input())
for _ in range(t):
    n = int(input())

    cnt = 0
    for x in p:
        if x > n // 2:
            break
        if not prime_num[n - x]:
            cnt += 1

    print(cnt)
