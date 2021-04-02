import math
def solution(brown, yellow):

    # 노란색을 기준으로 가로, 세로 찾기
    for x in range(1, int(math.sqrt(yellow)) + 1):
        y = yellow // x
        if x * y == yellow and 2 * x + 2 * y + 4 == brown:
            return [y + 2, x + 2]
