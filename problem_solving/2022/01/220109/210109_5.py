def check(num):
    global ans

    if num != "" and int(num) > n:
        return

    if num != "":
        ans = max(ans, int(num))

    for x in k:
        check(num + str(x))

n, m = map(int, input().split())
k = list(map(int, input().split()))

ans = -1
check("")
print(ans)