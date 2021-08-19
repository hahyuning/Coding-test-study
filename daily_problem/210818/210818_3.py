from collections import Counter
s = list(input())
s.sort()
s = Counter(s)

ans = ""
mid = ""
for i, x in s.items():
    if x % 2 == 0:
        ans += i * (x // 2)
    else:
        if len(mid) > 0:
            print("I'm Sorry Hansoo")
            break
        else:
            ans += i * (x // 2)
            mid = i
else:
    ans = ans + mid + ans[::-1]
    print(ans)
