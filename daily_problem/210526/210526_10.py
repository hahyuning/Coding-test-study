string = input()
a = []

prev = 0
for i in range(1, len(string)):
    if string[i] == ">":
        a.append(string[prev:i + 1])
        prev = i + 1
    elif string[i] == " ":
        if string[prev] == "<":
            continue
        a.append(string[prev:i])
        a.append(" ")
        prev = i + 1
    elif string[i] == "<":
        a.append(string[prev:i])
        prev = i
if prev < len(string):
    a.append(string[prev:])

ans = ""
for x in a:
    if x == "":
        continue

    if x[0] == "<":
        ans += x
    else:
        ans += x[::-1]

print(ans)