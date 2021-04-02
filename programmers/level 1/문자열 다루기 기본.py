def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for x in s:
            if not x.isdigit():
                answer = False
                break
    else:
        answer = False
    return answer