s = input()
a = []
words = ["w", "o", "l", "f"]
prev = 0
for i in range(1, len(s)):
    if s[i] == "w" and s[i - 1] != "w":
        a.append(s[prev:i])
        prev = i
a.append(s[prev:])

ans = True
for x in a:
    if len(x) % 4 != 0:
        ans = False
        break

    n = len(x) // 4
    cnt = 1
    for i in range(len(x)):
        if x[i] != words[i // n]:
            ans = False
            break

    if not ans:
        break

print(1 if ans else 0)

