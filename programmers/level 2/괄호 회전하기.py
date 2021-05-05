def solution(s):
    answer = 0
    for _ in range(len(s)):
        s = s[1:] + s[0]
        print(s)
        if check(s):
            answer += 1
    return answer

def check(string):
    stack = []
    for s in string:
        if s == "(" or s == "{" or s == "[":
            stack.append(s)
        else:
            if not stack:
                return False

            t = stack.pop()
            if s == ")":
                if t != "(":
                    return False
            elif s == "}":
                if t != "{":
                    return False
            elif s == "]":
                if t != "[":
                    return False

    if stack:
        return False
    return True

solution("}]()[{")