def solution(num):
    answer = 0

    while True:
        if num == 1:
            break
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        answer += 1

        if answer >= 500:
            return -1
    return answer