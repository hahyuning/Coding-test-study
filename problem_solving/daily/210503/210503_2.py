n = int(input())
ans = [0] * 10

power = 1
while n > 0:
    # 뒷자리가 9가 될때까지 숫자를 카운트하면서 1씩 감소시킨다.
    while n % 10 != 9:
        for x in str(n):
            ans[int(x)] += power
        n -= 1

    # n이 1자리 수인 경우
    if n < 10:
        for i in range(n + 1):
            ans[i] += power
        # 앞자리가 0인 경우 빼기
        ans[0] -= power
        break

    for i in range(10):
        ans[i] += (n // 10 + 1) * power
    # 앞자리가 0인 경우 빼기
    ans[0] -= power

    power = power * 10
    n //= 10

print(" ".join(map(str, ans)))

