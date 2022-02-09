n = int(input())

ans = 1
for i in range(1, n+1):
    ans *= i
    ans %= 1000000000000
    while ans % 10 == 0:
        ans //= 10
print(int(ans % 10))
