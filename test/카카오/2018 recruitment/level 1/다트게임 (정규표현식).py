import re

def solution(dartResult):
    # 정규표현식
    p = re.compile("(\d+)([A-Z])(\*|#)?")
    scores = p.findall(dartResult)
    print(scores)

    result = []
    for idx, score in enumerate(scores):
        point = score[0]
        bonus = score[1]
        option = score[2]

        # 보너스 계산
        if bonus == "S":
            bonus = 1
        elif bonus == "D":
            bonus = 2
        else:
            bonus = 3

        # 옵션 계산
        # 두배 시키기
        if option == "*":
            if idx != 0:
                result[idx - 1] *= 2
            result.append(int(point) ** bonus * 2)
        # 마이너스 하기
        elif option == "#":
            result.append(int(point) ** bonus * (-1))
        else:
            result.append(int(point) ** bonus)

    return sum(result)