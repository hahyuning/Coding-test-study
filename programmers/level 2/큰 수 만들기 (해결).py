def solution(number, k):
    answer = []

    for idx, num in enumerate(str(number)):

        # answer에서 num보다 작은 요소 전부 추출
        while answer and answer[-1] < num and k > 0:
            answer.pop()
            k -= 1

        # k개 만큼 제거한 경우 break
        if k == 0:
            answer += list(str(number))[idx:]
            break

        answer.append(num)

    # 제거해야 할 수가 남아있는 경우 뒤에서 자름
    if k > 0:
        answer = answer[:-k]

    return "".join(map(str, answer))

print(solution(4177252841, 4))