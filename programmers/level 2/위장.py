from collections import defaultdict

def solution(clothes):
    cloth_dic = defaultdict(list)
    for cloth, kind in clothes:
        cloth_dic[kind].append(cloth)

    answer = 1
    for x in cloth_dic.values():
        answer *= (len(x) + 1)

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))