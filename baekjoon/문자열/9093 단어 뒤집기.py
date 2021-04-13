n = int(input())

for _ in range(n):
    string = list(input().split())
    ans = []
    for x in string:
        ans.append(x[::-1])

    print(" ".join(ans))