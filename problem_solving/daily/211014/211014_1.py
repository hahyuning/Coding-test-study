s = input()
n = int(input())
cnt = list(map(int, input().split()))

tmp = s.split(" ")
s_list = []
for x in tmp:
    if x == "":
        continue

    tmp = ""
    for y in x:
        tmp += y.lower()
    s_list.append(tmp)

n -= (len(s_list) - 1)
if n < 0:
    print(-1)
else:
    for x in s_list:
        m = len(x)
        i = 0
        while i < m:
            now = x[i]
            cnt[ord(now) - ord("a")] -= 1
            while i < m and x[i] == now:
                i += 1

    for i in range(26):
        if cnt[i] < 0:
            print(-1)
            break
    else:
        ans = ""
        for x in s_list:
            ans += x[0].upper()

        for x in ans:
            cnt[ord(x) - ord("A")] -= 1
            if  cnt[ord(x) - ord("A")] < 0:
                print(-1)
                break
        else:
            print(ans)