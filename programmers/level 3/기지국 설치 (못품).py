def solution(n, stations, w):
    answer = 0

    x, y = divmod(stations[0] - w - 1, 2 * w + 1)
    answer += x
    if y != 0:
        answer += 1

    for i in range(len(stations)):
        if i == len(stations) - 1:
            if n - stations[i] - w < 0:
                continue
            else:
                x, y = divmod(n - stations[i] - w, 2 * w + 1)
        else:
            x, y = divmod(stations[i + 1] - stations[i] - 2 * w - 1, 2 * w + 1)
        answer += x
        if y != 0:
            answer += 1

    return answer