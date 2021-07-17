def solution(l):
    if l == 3:
        return ["  *  ", " * * ", "*****"]
    stars = solution(l // 2)
    tmp = []
    for s in stars:
        tmp.append(" " * (l // 2) + s + " " * (l // 2))
    for s in stars:
        tmp.append(s + " " + s)
    return tmp

n = int(input())
ans = solution(n)
for row in ans:
    print(row)