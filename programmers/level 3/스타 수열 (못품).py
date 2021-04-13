from collections import Counter


def solution(a):
    cnt = Counter(a)
    most_num = cnt.most_common(1)
    num = most_num[0][0]
    num_cnt = most_num[0][1]

    answer = 0
    i = 0
    while i < len(a) - 1:
        i += 1
        if a[i] == num and a[i - 1] == num:
            continue
        if a[i] != num and a[i - 1] != num:
            continue

        answer += 2
        i += 1

    return answer


print(solution([0]))
print(solution([5, 2, 3, 3, 5, 3]))
print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))
print(solution([0, 0, 3, 1, 2, 1, 3, 4, 0, 1, 4]))
