n, b = input().split()
n = n[::-1]
b = int(b)

ans = 0
for i in range(len(n)):
    if n[i].isdigit():
        ans += int(n[i]) * (b ** i)
    else:
        ans += (ord(n[i]) - ord("A") + 10) * (b ** i)

print(ans)