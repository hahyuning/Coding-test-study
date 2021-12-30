a = 0
b = 1

n = int(input())
if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    ans = 0
    for _ in range(n - 1):
        ans = a + b
        a = b
        b = ans
    print(ans)