t = int(input())
for _ in range(t):
    a, b = input().split()

    a = int(a, 2)
    b = int(b, 2)

    print(bin(a + b)[2:])