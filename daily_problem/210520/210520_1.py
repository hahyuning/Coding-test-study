n = int(input())
a = [int(input()) for _ in range(n)]
check = [True] * (n + 1)
ans = []
last = 0
check[0] = False

seq_check = False
for x in a:
    if last < x:
        cnt = sum(check[last + 1:x + 1])
        ans += ["+"] * cnt

        ans.append("-")
        check[x] = False

        for y in range(x - 1, -1, -1):
            if check[y] == True:
                last = y
                break
    elif last == x:
        ans.append("-")
        check[x] = False

        for y in range(x - 1, -1, -1):
            if check[y] == True:
                last = y
                break
    else:
        seq_check = True
        break

if seq_check:
    print("NO")
else:
    for x in ans:
        print(x)


