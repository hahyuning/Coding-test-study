def calculate(s):
    if s == "":
        return ""

    m = 0
    for x in s:
        if x == "M":
            m += 1
    if "K" in s:
        return str(5 * (10 ** m))
    else:
        return str(10 ** (m - 1))

s = input()

max = ""
prev = ""
for i in range(len(s)):
    if s[i] == "K":
        prev += s[i]
        max += calculate(prev)
        prev = ""
    else:
        if "K" in s[i:]:
            prev += s[i]
        else:
            max += "1" * (len(s) - i)
            prev = ""
            break

max += calculate(prev)
print(max)

min = ""
prev = ""
for i in range(len(s)):
    if s[i] == "K":
        min += calculate(prev)
        min += calculate(s[i])
        prev = ""
    else:
        prev += s[i]

min += calculate(prev)
print(min)