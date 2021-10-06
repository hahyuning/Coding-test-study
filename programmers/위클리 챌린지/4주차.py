def solution(table, languages, preference):
    scores = dict()
    for x in table:
        job, *score = x.split()
        scores[job] = score

    res = []
    for job, score in scores.items():
        tmp = 0
        for i, lan in enumerate(languages):
            if lan in score:
                tmp += preference[i] * (5 - score.index(lan))
        res.append((tmp, job))
    res.sort(key=lambda x: (-x[0], x[1]))

    return res[0][1]