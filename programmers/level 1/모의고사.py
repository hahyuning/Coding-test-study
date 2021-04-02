def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1_len = len(s1)
    s2_len = len(s2)
    s3_len = len(s3)

    s1_score = 0
    s2_score = 0
    s3_score = 0
    for i, x in enumerate(answers):
        if x == s1[i % s1_len]:
            s1_score += 1
        if x == s2[i % s2_len]:
            s2_score += 1
        if x == s3[i % s3_len]:
            s3_score += 1

    max_score = max(s1_score, s2_score, s3_score)
    if s1_score == max_score:
        answer.append(1)
    if s2_score == max_score:
        answer.append(2)
    if s3_score == max_score:
        answer.append(3)
    return answer

print(solution([1, 2, 3, 4, 5]))