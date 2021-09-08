def solution(n, t, m, timetable):
    timetable = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]
    timetable.sort()

    for i in range(n):
        #마지막 운행 시간
        last_time = 540 + (n - 1) * t

        #대기열에 있는 크루의 수가 버스 정원보다 작다면 마지막 셔틀시간 반환
        if len(timetable) < m:
            return '%02d:%02d' % (last_time // 60, last_time % 60)

        #마지막 셔틀버스
        if i == n - 1:
            #대기열에 가장 처음에 있는 사람의 시간이 마지막 셔틀시간보다 크다면
            #마지막 셔틀버스 시간 반환
            if timetable[0] > last_time:
                return '%02d:%02d' % (last_time // 60, last_time % 60)
            #대기열의 가장 처음에 있는 사람의 시간이 마지막 셔틀시간보다 작거나 같으면
            #m번째 타는 크루의 시간보다 1초 작은 시간 반환
            time = timetable[m - 1] - 1
            return '%02d:%02d' % (time // 60, time % 60)

        #버스 운행 시간마다 m명씩 승객 태우고 timetable에서 삭제
        for j in range(m - 1, -1, -1):
            bus_arrive = 540 + i * t
            if timetable[j] <= bus_arrive:
                del timetable[j]