n = int(input())
l = list(map(int, input().split()))

if n == 0:
    print(0)
elif n == 1:
    print(l[0])
else:
    # 가장 큰 레벨의 카드는 마지막까지 남기는 게 좋다.
    ans = 0
    while len(l) >= 2:
        std = max(l)
        std_id = l.index(std)

        if std_id == 0:
            x = l.pop(1)
        elif std_id == len(l) - 1:
            x = l.pop(std_id - 1)
        else:
            a = l[std_id - 1]
            b = l[std_id + 1]
            if a < b:
                x = a
                l.pop(std_id - 1)
            else:
                x = b
                l.pop(std_id + 1)

        ans += (std + x)
    print(ans)

