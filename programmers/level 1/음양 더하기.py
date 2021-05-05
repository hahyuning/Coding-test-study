def solution(absolutes, signs):
    answer = 0
    for sign, num in zip(signs, absolutes):
        if sign:
            answer += num
        else:
            answer -= num
    return answer