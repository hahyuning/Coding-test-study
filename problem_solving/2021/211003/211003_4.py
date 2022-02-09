import datetime
from datetime import timedelta

for _ in range(3):
    s, t = input().split()

    s_split = list(map(int, s.split(":")))
    t_split = list(map(int, t.split(":")))

    s_time = datetime.datetime(2021, 1, 1, s_split[0], s_split[1], s_split[2])
    tmp = s_time.strftime("%H%M%S")
    t_time = datetime.datetime(2021, 1, 1, t_split[0], t_split[1], t_split[2])
    t_time = t_time.strftime("%H%M%S")

    sec = 1
    cnt = 0

    while True:
        if int(tmp) % 3 == 0:
            cnt += 1

        if tmp == t_time:
            break

        s_time += timedelta(seconds=sec)
        tmp = s_time.strftime("%H%M%S")

    print(cnt)
