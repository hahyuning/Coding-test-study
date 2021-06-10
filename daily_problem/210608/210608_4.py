n = int(input())
limit = list(map(int, input().split()))
m = int(input())
weight = list(map(int, input().split()))

limit.sort(reverse=True)
weight.sort(reverse=True)

if weight[0] > limit[0]:
    print(-1)
else:
    ans = 0
    while weight:
        ans += 1
        for x in limit:
            if not weight:
                break

            for y in weight:
                if x >= y:
                    weight.remove(y)
                    break
    print(ans)