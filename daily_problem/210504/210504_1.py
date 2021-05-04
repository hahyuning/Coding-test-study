n = int(input())
a = [input() for _ in range(n)]
a.sort(key=len)

ans = 0
for i in range(n):
    flg = False
    for j in range(i + 1, n):
        try:
            # 접두사 확인
            if a[j].index(a[i]) == 0:
                flg = True
                break
        except:
            continue

    if flg == False:
        ans += 1
print(ans)
