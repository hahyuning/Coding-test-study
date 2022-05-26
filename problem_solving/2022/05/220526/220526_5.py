s = input()

while len(s) % 3 != 0:
    s = "0" + s

ans = ""
for i in range(len(s), 0, -3):
    t = s[i - 3:i]

    tmp = 0
    for k in range(3):
        tmp += int(t[k]) * 2 ** (2 - k)

    ans = str(tmp) + ans
print(ans)

