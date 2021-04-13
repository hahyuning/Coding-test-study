string = list(input())
ans = []

for s in string:
    ascii_s = ord(s) - 3
    if ascii_s < 65:
        ascii_s += 26
    ans.append(chr(ascii_s))

print("".join(ans))