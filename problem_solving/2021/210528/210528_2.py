s = input()
t = input()

ans = 0
while len(s) > 0:
    if s[0] != t[0]:
        s = s[1:]
        continue

    if len(s) < len(t):
        break

    check = False
    for i in range(len(t)):
        if s[i] != t[i]:
            check = True
            break

    if check:
        s = s[1:]
    else:
        ans += 1
        s = s[len(t):]

print(ans)
