num = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]

t = int(input())
for _ in range(t):
    n = int(input())

    if n < 11:
        print(num[n], end=" ")

        max_val = [1 for i in range(n // 2)]
        if n % 2 == 1:
            max_val[0] = 7
        print("".join(map(str, max_val)))
    else:
        min_val = [8 for i in range((n + 6) // 7)]
        if n % 7 == 1:
            min_val[0] = 1
            min_val[1] = 0
        elif n % 7 == 2:
            min_val[0] = 1
        elif n % 7 == 3:
            min_val[0] = 2
            min_val[1] = 0
            min_val[2] = 0
        elif n % 7 == 4:
            min_val[0] = 2
            min_val[1] = 0
        elif n % 7 == 5:
            min_val[0] = 2
        elif n % 7 == 6:
            min_val[0] = 6
        print("".join(map(str, min_val)))

        max_val = [1 for i in range(n // 2)]
        if n % 2 == 1:
            max_val[0] = 7
        print("".join(map(str, max_val)))

