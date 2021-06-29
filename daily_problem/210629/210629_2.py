a = input()
b = input()

s = ""
for x in a:
    if x.isalpha():
        s += x

if b in s:
    print(1)
else:
    print(0)