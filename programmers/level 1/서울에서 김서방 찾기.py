def solution(seoul):
    answer = 0

    for x in seoul:
        if x == "Kim":
            break
        answer += 1

    return "김서방은 {}에 있다".format(answer)