n = int(input())
num = list(map(int, input().split()))

if n == 1:
    print("A")
elif n == 2:
    if num[0] != num[1]:
        print("A")
    else:
        print(num[0])
else:
    if num[0] == num[1]:
        a = 0
    else:
        a = (num[1] - num[2]) // (num[0] - num[1])

    b = num[1] - a * num[0]

    for i in range(n - 1):
        nxt = a * num[i] + b
        if num[i + 1] != nxt:
            print("B")
            break
    else:
        print(a * num[-1] + b)
