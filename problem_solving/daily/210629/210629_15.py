s = input()
ans = ""
for x in s:
    if not x.isalpha():
        ans += x
        continue
    tmp = ord(x) + 13
    if x.isupper():
        if tmp > 90:
            tmp -= 26
    else:
        if tmp > 122:
            tmp -= 26
    ans += chr(tmp)
print(ans)