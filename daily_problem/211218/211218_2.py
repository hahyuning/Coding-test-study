import sys
input = sys.stdin.readline

s_dic = {"-":0, "\\":1, "(":2, "@":3, "?":4, ">":5, "&":6, "%":7, "/":-1}
while True:
    s = input().rstrip()
    if s == "#":
        break

    s = s[::-1]
    i = 0
    ans = 0
    for x in s:
        ans += (8 ** i) * s_dic[x]
        i += 1
    print(ans)
