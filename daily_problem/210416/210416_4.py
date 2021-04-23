a, b = map(int, input().split())
num = []
for i in range(1, 1001):
    num += [i] * i

print(sum(num[a - 1:b]))