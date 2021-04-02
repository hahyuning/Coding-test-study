def solution(arr1, arr2):
    answer = []
    n = len(arr1)
    m = len(arr1[0])

    for x in range(n):
        list = []
        for y in range(m):
            list.append(arr1[x][y] + arr2[x][y])
        answer.append(list)
    return answer