t = int(input())
for _ in range(t):
    d, n = map(int, input().split())
    a = list(map(int, input().split()))

    s = [0] * n
    cnt = [0] * d

    s[0] = a[0]
    cnt[s[0] % d] += 1
    for i in range(1, n):
        s[i] = s[i - 1] + a[i]
        cnt[s[i] % d] += 1

    ans = cnt[0]
    for i in range(d):
        ans += (cnt[i] * (cnt[i] - 1)) // 2
    print(ans)