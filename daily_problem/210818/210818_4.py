s = input()
ans = set()

n = len(s)
for k in range(1, n + 1):
    for i in range(n):
        tmp = s[i:i + k]
        ans.add(tmp)
print(len(ans))