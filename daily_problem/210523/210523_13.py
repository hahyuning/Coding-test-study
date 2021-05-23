n = int(input())
d = [0] * (n + 1)
d[2] = 1

for i in range(5, n + 1):
    if d[i - 1] == 0 and d[i - 3] == 0 and d[i - 4] == 0:
        d[i] = 1

if d[n] == 1:
    print("CY")
else:
    print("SK")