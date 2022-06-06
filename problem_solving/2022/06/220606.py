import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keyword = dict()
for _ in range(n):
    x = input().rstrip()
    keyword[x] = True

ans = n
for _ in range(m):
    a = input().split(",")
    for x in a:
        if x in keyword and keyword[x]:
            ans -= 1
            keyword[x] = False

    print(ans)