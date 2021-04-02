from collections import defaultdict
def solution(participant, completion):
    answer = ''
    participant_dic = defaultdict(int)
    for x in participant:
        participant_dic[x] += 1
    for y in completion:
        participant_dic[y] -= 1

    for x, y in participant_dic.items():
        if y == 1:
            answer = x
    return answer