s = input().split(":")
ans = []
for i in range(len(s)):
    if len(s[i]) == 4:
        ans.append(s[i])
    elif s[i] == "":
        if len(ans) + len(s) - i - 1 == 8:
            continue
        else:
            zero = 8 - len(ans) - len(s) + i + 1
            for _ in range(zero):
                ans.append("0000")
    elif len(s[i]) < 4:
        tmp = s[i][::-1]
        zero = 4 - len(tmp)
        tmp += "0" * zero
        ans.append(tmp[::-1])

print(":".join(ans))