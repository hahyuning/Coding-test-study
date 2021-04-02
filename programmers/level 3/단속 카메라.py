def solution(routes):
    routes.sort()

    cctv = routes[0][1]
    routes.pop(0)
    answer = 1

    for route in routes:
        # 경로의 시작 지점이 현재 cctv의 위치보다 이전에 있으면
        # cctv의 위치를 경로의 끝 지점과, cctv의 위치의 최솟값으로 변경
        if route[0] <= cctv:
            cctv = min(route[1], cctv)
        else:
            cctv = route[1]
            answer += 1
    return answer