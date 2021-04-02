def solution(numbers):
    answer = []
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            t1 = numbers[i]
            t2 = numbers[j]
            if t1 + t2 not in answer:
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer