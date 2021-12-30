s = input()
t = input()

n = len(s)
m = len(t)

if n > m:
    k = n // m
    t = t * k + t[:n % m]
else:
    t = t[:n]

ans = ""
for i in range(n):
    if s[i] == " ":
        ans += " "
        continue

    num = ord(t[i]) - ord("a") + 1
    num = ord(s[i]) - ord("a") + 1 - num
    if num <= 0:
        num += 26

    ans += chr(num + 96)

print(ans)