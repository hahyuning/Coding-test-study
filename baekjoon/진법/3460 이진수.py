n = int(input())

for _ in range(n):
    num = int(input())

    i = 0
    while num > 1:
        if  num % 2 == 1:
            print(i, end=" ")
        i += 1
        num //= 2
    if num == 1:
        print(i)