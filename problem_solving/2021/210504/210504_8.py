a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

if p <= c:
    print(min(p * a, b))
else:
    print(min(p * a, (p - c) * d + b))