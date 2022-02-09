s = input()
# l[i]: i번째 R의 왼쪽에 있는 K의 개수
l = []
# r[i]: i번째 R의 오른쪽에 있는 K의 개수
r = []

l_cnt = 0
r_cnt = 0
for i in range(len(s)):
    if s[i] == "K":
        l_cnt += 1
    else:
        l.append(l_cnt)

    if s[len(s) - i - 1] == "K":
        r_cnt += 1
    else:
        r.append(r_cnt)
r.reverse()

lt, rt = 0, len(l) - 1
ans = 0
while lt <= rt:
    ans = max(ans, rt - lt + 1 + 2 * min(l[lt], r[rt]))
    if l[lt] < r[rt]:
        lt += 1
    else:
        rt -= 1
print(ans)