# 균형잡힙 문자열의 최소 인덱스 반환
def balanced(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

# 올바른 문자열인지 확인
def proper(p):
    cnt = 0
    for x in p:
        if x == "(":
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True

def solution(p):
    if p == "":
        return ""

    i = balanced(p)
    u = p[:i + 1]
    v = p[i + 1:]

    if proper(u):
        ans = u + solution(v)
    else:
        ans = "("
        ans += solution(v)
        ans += ")"

        u = list(u[1:-1])
        change = {"(":")", ")":"("}
        for i in range(len(u)):
            u[i] = change[u[i]]
        ans += "".join(u)

    return ans