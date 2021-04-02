def solution(s):
    answer = True
    p_num = 0
    y_num = 0
    for x in s:
        if x.lower() == "p":
            p_num += 1
        elif x.lower() == "y":
            y_num += 1

    if p_num != y_num:
        answer = False
    return answer