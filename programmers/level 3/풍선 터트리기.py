# 각 숫자의 왼쪽과 오른쪽 최솟값 중 하나라도 해당 숫자보다 클 경우
# 마지막까지 남길 수 있다.
def solution(a):
    result = [False for _ in range(len(a))]
    left_min, right_min = 10 ** 9 + 1, 10 ** 9 + 1

    for i in range(len(a)):
        if a[i] < left_min:
            left_min = a[i]
            result[i] = True

    for i in range(len(a) - 1, -1, -1):
        if a[i] < right_min:
            right_min = a[i]
            result[i] = True
    return sum(result)


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))