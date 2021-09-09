n = int(input())

if n == 0:
    print(0)
else:
    ans = ""
    while n != 0:
        if n % (-2) == 0:
            ans += "0"
            n //= (-2)
        else:
            ans += "1"
            n //= (-2)
            n += 1
    print(ans[::-1])