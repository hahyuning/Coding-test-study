def solution(numbers):
    numbers = list(map(str, numbers))
    # 숫자의 범위가 최대 1000이므로 각각의 자리(4자리)로 정렬
    answer = "".join(sorted(numbers, key=lambda x: (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]), reverse=True))
    if int(answer) == 0:
        return "0"

    return answer