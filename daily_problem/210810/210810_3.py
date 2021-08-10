n = int(input())
h = list(map(int, input().split()))
s = sum(h)

if s % 3 != 0:
    print("NO")
else:
    x = s // 3
    y = 0
    for apple in h:
        y += apple // 2

    if x > y:
        print("NO")
    else:
        print("YES")