s = list(map(int, input().split(":")))
e = list(map(int, input().split(":")))
s_time = 0
e_time = 0

for i in range(3):
    s_time += s[i] * (60 ** (2 - i))
    e_time += e[i] * (60 ** (2 - i))

if s == e:
    print("24:00:00")
else:
    if s > e:
        ans = 24 * 3600
        ans -= s_time
        ans += e_time
    else:
        ans = e_time - s_time

    res = ""
    for i in range(3):
        tmp = str(ans // (60 ** (2 - i)))
        ans %= (60 ** (2 - i))
        if len(tmp) == 1:
            tmp = "0" + tmp
        if i == 2:
            res += tmp
        else:
            res += tmp + ":"
    print(res)