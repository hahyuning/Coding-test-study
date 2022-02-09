n = int(input())
h = list(map(int, input().split()))

ans = 0
arrow = [0] * (max(h) + 2)
for i in range(n):
    height = h[i]
    if arrow[height] > 0:
        arrow[height] -= 1
        arrow[height - 1] += 1
    else:
        ans += 1
        arrow[height - 1] += 1
print(ans)