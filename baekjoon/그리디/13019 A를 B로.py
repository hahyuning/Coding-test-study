s = input()
t = input()

cnt1 = [0] * 26
cnt2 = [0] * 26
for i in range(len(s)):
    cnt1[ord(s[i]) - ord("A")] += 1
    cnt2[ord(t[i]) - ord("A")] += 1

ans = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == t[len(s) - 1 - ans]:
        ans += 1

if cnt1 != cnt2:
    print(-1)
else:
    print(len(s) - ans)