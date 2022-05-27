s = input()
t = input()

ans = 0
while len(s) != len(t):
    if t[-1] == "A":
        t = t[:-1]
    else:
        t = t[:-1][::-1]

    if s == t:
        ans = 1
        break

print(ans)