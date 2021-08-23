n = int(input())
s = input()
bs, be = -1, -1
rs, re = -1, -1

for i in range(n):
    if s[i] == "B":
        if bs == -1:
            bs = i
        be = i
    if s[i] == "R":
        if rs == -1:
            rs = i
        re = i

cnt1 = 1
for i in range(bs, be):
    if s[i] == "R" and s[i - 1] == "B":
        cnt1 += 1
if bs != 0:
    cnt1 += 1
if be != n - 1:
    cnt1 += 1

cnt2 = 1
for i in range(rs, re):
    if s[i] == "B" and s[i - 1] == "R":
        cnt2 += 1
if rs != 0:
    cnt2 += 1
if re != n - 1:
    cnt2 += 1

print(min(cnt1, cnt2))