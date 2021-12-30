s = input()
d = [0] * (len(s) + 1)

if s[0] == "0":
    print(0)
else:
    d[0] = 1
    d[1] = 1
    for i in range(2, len(s) + 1):
        if int(s[i - 1]) != 0:
            d[i] = d[i - 1]
        if 10 <= int(s[i - 2:i]) <= 26:
            d[i] += d[i - 2]
        d[i] %= 1000000
    print(d[len(s)])