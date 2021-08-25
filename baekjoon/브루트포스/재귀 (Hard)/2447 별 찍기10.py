def solution(l):
    if l == 1:
        return ["*"]
    stars = solution(l // 3)
    tmp = []
    for s in stars:
        tmp.append(s * 3)
    for s in stars:
        tmp.append(s + " " * (l // 3) + s)
    for s in stars:
        tmp.append(s * 3)
    return tmp

n = int(input())
ans = solution(n)
for row in ans:
    print(row)