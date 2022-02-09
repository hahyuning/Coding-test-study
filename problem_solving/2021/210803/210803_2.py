n, q = map(int, input().split())
a = list(map(int, input().split()))
a += a[:3]
mul = []

for i in range(0, len(a) - 3):
    mul.append(a[i] * a[i + 1] * a[i + 2] * a[i + 3])

q_list = list(map(int, input().split()))
m = len(mul)
ans = sum(mul)
for x in q_list:
    for i in [x - 1, x - 2, x - 3, x - 4]:
        if i < 0:
            i += m
        mul[i] *= (-1)
        ans += 2 * mul[i]
    print(ans)