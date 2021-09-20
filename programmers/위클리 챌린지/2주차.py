def solution(scores):
    n = len(scores)
    ans = []
    for j in range(n):
        me = scores[j][j]
        s = 0
        cnt = n
        min_val = 100
        max_val = 0
        tmp = []

        for i in range(n):
            tmp.append(scores[i][j])
            s += scores[i][j]
            max_val = max(max_val, scores[i][j])
            min_val = min(min_val, scores[i][j])

        if me == min_val and tmp.count(min_val) == 1:
            s -= me
            cnt -= 1
        if me == max_val and tmp.count(max_val) == 1:
            s -= me
            cnt -= 1

        ans.append(s / cnt)

    res = ""
    for x in ans:
        if x >= 90:
            res += "A"
        elif x >= 80:
            res += "B"
        elif x >= 70:
            res += "C"
        elif x >= 50:
            res += "D"
        else:
            res += "F"
    return res

solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])