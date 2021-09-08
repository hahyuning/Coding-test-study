def solution(numbers, hand):
    answer = ''
    # 0부터 9까지 좌표
    array = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    # 왼손 시작
    left = [3, 0]
    # 오른쪽 시작
    right = [3, 2]

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += "L"
            left = array[num]
        elif num == 3 or num == 6 or num == 9:
            answer += "R"
            right = array[num]
        else:
            res = distance(array[num], left, right, hand)
            if res == "right":
                answer += "R"
                right = array[num]
            else:
                answer += "L"
                left = array[num]
    return answer

def distance(target, left, right, hand):
    left_dist = 0
    right_dist = 0
    for i in range(2):
        left_dist += abs(left[i] - target[i])
        right_dist += abs(right[i] - target[i])

    if left_dist > right_dist:
        return "right"
    elif left_dist < right_dist:
        return "left"
    else:
        return hand