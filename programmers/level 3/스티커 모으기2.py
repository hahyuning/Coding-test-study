def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    # d[i]: 0~i 번째 스티커 스티커를 떼는 경우의 최대값
    # d[i] = max(d[i - 2] + sticker[i], d[i - 1])

    # 주의할 점: 첫 번째 스티커를 떼냐 마냐에 따라 마지막 스티커 확인 여부가 달라진다.
    # 1. 첫 번째 스티커를 뗀 경우
    d = [0] * len(sticker)
    d[0] = d[1] = sticker[0]

    for i in range(2, len(sticker) - 1):
        d[i] = max(d[i - 2] + sticker[i], d[i - 1])

    answer = max(d)
    # 2. 첫 번째 스티커를 안 뗀 경우
    d = [0] * len(sticker)
    d[1] = sticker[1]

    for i in range(2, len(sticker)):
        d[i] = max(d[i - 2] + sticker[i], d[i - 1])

    return max(answer, max(d))

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))