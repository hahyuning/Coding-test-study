s = input()
pikachu = ["pi", "ka", "chu"]
while len(s) > 0:
    if s[:2] in pikachu:
        s = s[2:]
    elif s[:3] in pikachu:
        s = s[3:]
    else:
        print("NO")
        break
else:
    print("YES")