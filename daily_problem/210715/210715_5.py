n, k = map(int, input().split())

cnt = 0
for h in range(0, n + 1):
    for m in range(0, 60):
        for s in range(0, 60):
            if h == 0:
                hh = "00"
            elif 0 < h < 10:
                hh = "0" + str(h)
            else:
                hh = str(h)

            if m == 0:
                mm = "00"
            elif 0 < m < 10:
                mm = "0" + str(m)
            else:
                mm = str(m)

            if s == 0:
                ss = "00"
            elif 0 < s < 10:
                ss = "0" + str(s)
            else:
                ss = str(s)

            if str(k) in hh + mm + ss:
                cnt += 1

print(cnt)