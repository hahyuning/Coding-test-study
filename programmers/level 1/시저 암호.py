def solution(s, n):
    answer = ''
    for x in s:
        if x != " ":
            asc = ord(x) + n
            if x.isupper():
                if asc > 90:
                    asc -= 26
            else:
                if asc > 122:
                    asc -= 26
            answer += chr(asc)
        else:
            answer += " "
    return answer

print(solution("AB", 1))