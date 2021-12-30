n = int(input())
ans = 0
ans += n // 5
n %= 5

if n % 2 == 0:
    ans += n // 2
    print(ans)
else:
    if ans == 0:
        print(-1)
    else:
        ans -= 1
        n += 5
        ans += n // 2
        print(ans)