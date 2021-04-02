def solution(arr):
    answer = []
    for x in arr:
        if len(answer) == 0:
            answer.append(x)
        elif answer[-1] == x:
            continue
        else:
            answer.append(x)
    return answer