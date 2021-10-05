from collections import defaultdict

n = int(input())
s = input()

check = defaultdict(int)
ans = 0
lt, rt = 0, 0
while lt < len(s) and rt < len(s):
    check[s[rt]] += 1

    if len(check) > n:
        while lt <= rt and len(check) > n:
            check[s[lt]] -= 1
            if check[s[lt]] == 0:
                del check[s[lt]]
            lt += 1
    if len(check) <= n:
        ans = max(ans, rt - lt + 1)

    rt += 1

print(ans)