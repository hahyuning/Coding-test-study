s = input()
n = len(s)
ans = []
for i in range(n - 1):
    for j in range(i, n - 1):
        if i == j:
            continue

        tmp = [s[:i + 1], s[i + 1:j + 1], s[j + 1:]]
        t = ""
        for x in tmp:
            t += x[::-1]
        ans.append(t)
ans.sort()
print(ans[0])
