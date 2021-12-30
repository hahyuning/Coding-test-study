def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

n = int(input())
a = list(map(int, input().split()))
x = int(input())

tmp = []
for y in a:
    if gcd(x, y) == 1:
        tmp.append(y)

print(sum(tmp) / len(tmp))