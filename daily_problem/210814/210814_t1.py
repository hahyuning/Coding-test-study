def solution(name_list):
    answer = []
    check = dict()
    for x in name_list:
        if x not in check:
            answer.append(x + "A")
            check[x] = 0
        else:
            num = check[x] + 1
            answer.append(x + str(chr(num + ord("A"))))
            check[x] += 1

    return answer

solution(["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"])