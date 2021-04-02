def solution(progresses, speeds):
    answer = []
    progresses = [100 - x for x in progresses]
    pnt = 0

    while True:
        if sum(progresses) == 0:
            break

        for i in range(pnt, len(progresses)):
            progresses[i] = max(0, progresses[i] - speeds[i])

        cnt = 0
        for i in range(pnt, len(progresses)):
            if progresses[i] != 0:
                break
            cnt += 1
            pnt += 1

        if cnt != 0:
            answer.append(cnt)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))