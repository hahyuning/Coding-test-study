n = int(input())
ans = 0
start, length = 1, 1

while start <= n:
    end = start * 10 - 1
    end = min(n, end)

    ans += (end - start + 1) * length
    start *= 10
    length += 1

print(ans)