import sys

s = input()
k = int(input())
d = []
d.append("()")

for l in range(4, len(s) + 1, 2):
    # 길이가 l인 좋은 문자열 찾기
    for i in range(len(d)):
        now = d[i]
        if (l - 2) % len(now) == 0:
            nxt = "(" + now * ((l - 2) // len(now)) + ")"
            d.append(nxt)
d.sort()

# s의 부분수열인지 확인
for x in d:
    idx = 0
    i = 0

    while idx < len(x) and i < len(s):
        if x[idx] == s[i]:
            idx += 1
        i += 1
    if idx == len(x):
        k -= 1
        if k == 0:
            print(x)
            sys.exit(0)
print(-1)