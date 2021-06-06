a = list(map(int, input().split()))
odd = []
even = []
for i in range(3):
    if a[i] % 2 != 0:
        odd.append(a[i])
    else:
        even.append(a[i])

ans = 1
if odd:
    for x in odd:
        ans *= x
else:
    for x in even:
        ans *= x

print(ans)