t = int(input())
for _ in range(t):
    n, m = input().split()

    zero, one = 0, 0
    for i in range(len(n)):
        if n[i] != m[i]:
            if m[i] == "0":
                zero += 1
            else:
                one += 1

    swap = min(zero, one)
    print(zero + one - swap)
