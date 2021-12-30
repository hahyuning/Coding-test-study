n = int(input())
born = [0] * (n + 1)
born[1] = 1
d = [0] * (n + 1)
d[1] = 1

for i in range(2, n + 1):
    d[i] = 2 * d[i - 1]
    born[i] = d[i - 1]
    if i % 2 == 0:
        if i - 3 >= 0:
            d[i] -= born[i - 3]
        if i - 4 >= 0:
            d[i] -= born[i - 4]

print(d[n])