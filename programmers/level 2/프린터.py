def solution(priorities, location):
    answer = 0

    while len(priorities) > 0:
        x = priorities.pop(0)
        location -= 1

        if not priorities:
            answer += 1
            break
        if x < max(priorities):
            priorities.append(x)
            if location < 0:
                location = len(priorities) - 1
        else:
            answer += 1
            if location == -1:
                break
    return answer
