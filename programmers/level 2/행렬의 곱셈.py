def solution(arr1, arr2):
    answer = []
    n = len(arr1)
    m = len(arr2[0])
    l = len(arr1[0])
    for i in range(n):
        list = []
        for k in range(m):
            c = 0
            for j in range(l):
                c += arr1[i][j] * arr2[j][k]
            list.append(c)
        answer.append(list)
    return answer