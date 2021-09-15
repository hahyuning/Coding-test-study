# 셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다.
# 셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발한다.

# 콘이 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각을 구하여라.
# 콘은 게으르기 때문에 같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다.
# 또한, 모든 크루는 잠을 자야 하므로 23:59에 집에 돌아간다. 따라서 어떤 크루도 다음날 셔틀을 타는 일은 없다.

def print_time(t):
    return str(t // 60).zfill(2) + ":" + str(t % 60).zfill(0)

def solution(n, t, m, timetable):
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()

    now = 540
    idx = 0
    cnt = 0
    for i in range(n):
        cnt = 0
        while True:
            if idx >= len(timetable):
                break
            if cnt == m:
                break
            if timetable[idx] > now:
                break
            cnt += 1
            idx += 1
        now += t

    # 마지막 셔틀에 탑승하는 승객이 m명일 경우
    # 마지막 사람보다 1분 전에 도착
    if cnt == m:
        return print_time(timetable[idx - 1] - 1)
    # 마지막 셔틀에 탑승하는 승객이 m명 미만인 경우
    # 마지막 셔틀 시간에 도착
    return print_time(now - t)
