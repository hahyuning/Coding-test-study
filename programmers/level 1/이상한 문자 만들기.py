def solution(s):
    answer = ''
    cnt = 0
    for x in s:
        if x == " ":
            answer += " "
            cnt = 0

        elif cnt % 2 == 0:
            answer += x.upper()
            cnt += 1
        else:
            answer += x.lower()
            cnt += 1
    return answer