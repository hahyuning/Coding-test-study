import heapq


def solution(jobs):
    answer = 0
    now = 0  # 하나의 작업이 큐에서 나온 시간
    last = -1  # 하나의 작업이 큐에 들어간 시간
    cnt = 0  # 완료한 작업 수
    wait = []
    while cnt < len(jobs):

        for job in jobs:
            if last < job[0] <= now:
                answer += now - job[0]
                heapq.heappush(wait, job[1])

        if len(wait) > 0:
            answer += len(wait) * wait[0]

            last = now
            now += heapq.heappop(wait)
            cnt += 1
        else:
            now += 1

    return answer // len(jobs)