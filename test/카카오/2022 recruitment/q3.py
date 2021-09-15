from collections import defaultdict
import math

def solution(fees, records):
    ans = []

    time = defaultdict(list)
    out_check = dict()
    for r in records:
        x, num, op = r.split(" ")
        num = int(num)
        h, m = map(int, x.split(":"))
        t = h * 60 + m
        if op == "IN":
            out_check[num] = False
            time[num].append(t)
        else:
            out_check[num] = True
            prev = time[num].pop()
            tmp = 0
            if len(time[num]) > 0:
                tmp = time[num].pop()

            time[num].append((t - prev + tmp))

    order = list(time.keys())
    order.sort()

    end_t = 23 * 60 + 59
    for key in order:
        val = time[key]
        if not out_check[key]:
            prev = val.pop()
            tmp = 0
            if len(val) > 0:
                tmp = val.pop()
            t = end_t - prev + tmp
        else:
            t = val[0]

        if t <= fees[0]:
            ans.append(fees[1])
        else:
            tmp = fees[1] + math.ceil((t - fees[0]) / fees[2]) * fees[3]
            ans.append(tmp)

    return ans

solution([1, 461, 1, 10], ["00:00 1234 IN"])