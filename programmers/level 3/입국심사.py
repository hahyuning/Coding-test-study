def solution(n, times):
    answer = 0
    times.sort()
    lt = min(times)
    rt = max(times) * (n // len(times) + 1)
    while lt <= rt:
        mid = (lt + rt) // 2
        if Count(mid, times) >= n:
            answer = mid
            rt = mid - 1
        else:
            lt = mid + 1
    return answer

def Count(time, times):
    people = 0
    for x in times:
        people += time // x
    return people