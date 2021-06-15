s = input()

n = len(s)
for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        print(n)
        break
else:
    for i in range(1, n):
        if s[0] != s[i]:
            check = True
            print(n - 1)
            break
    else:
        print(-1)
