n = int(input())
# 소수일 경우 False, 소수가 아닐 경우 True
prime_check = [False] * (n + 1)
primes = []
for i in range(2, n + 1):
    if prime_check[i] == True:
        continue

    primes.append(i)
    j = i * 2
    while j <= n:
        prime_check[j] = True
        j += i

left, right = 0, 0
cnt = 0
sum = 0
if len(primes) != 0:
    sum = primes[0]

while left <= right and right < len(primes):
    if sum <= n:
        if sum == n:
            cnt += 1

        right += 1
        if right < len(primes):
            sum += primes[right]

    else:
        sum -= primes[left]
        left += 1

        # primes가 오름차순이므로 이 부분은 생략 가능할지도
        if left > right and left < len(primes):
            right = left
            sum = primes[left]

print(cnt)