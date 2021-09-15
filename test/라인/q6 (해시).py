from collections import defaultdict, Counter

def solution(records, k, date):
    date_record = {i:[] for i in range(1, 13)}

    for r in records:
        time, user_id, item_id = r.split()
        w, m, d = map(int, time.split("-"))
        user_id = int(user_id[3:])
        item_id = int(item_id[3:])
        date_record[m].append((d, user_id, item_id))

    ew, em, ed = map(int, date.split("-"))
    m_diff = k // 30
    d_diff = k % 30

    if ed - d_diff <= 0:
        sd = ed - d_diff + 31
        sm = em - m_diff - 1
    else:
        sd = ed - d_diff + 1
        sm = em - m_diff

    if sm <= 0:
        sm = 1
        sd = 1

    all_item = defaultdict(list)

    if sm == em:
        for day, user_id, item_id in date_record[sm]:
            if sd <= day <= ed:
                all_item[item_id].append(user_id)
    else:
        for month in range(sm, em + 1):
            if month == sm:
                for day, user_id, item_id in date_record[month]:
                    if sd <= day:
                        all_item[item_id].append(user_id)
            elif month == em:
                for day, user_id, item_id in date_record[month]:
                    if day <= ed:
                        all_item[item_id].append(user_id)
            else:
                for day, user_id, item_id in date_record[month]:
                    all_item[item_id].append(user_id)

    ans = []
    for item_id, user_ids in all_item.items():
        all_cnt = len(user_ids)
        c_list = Counter(user_ids)
        re_cnt = len(c_list.keys())
        percent = (all_cnt / re_cnt) * 100
        ans.append((percent, all_cnt, item_id))

    if not ans:
        return ["no result"]

    ans.sort(key=lambda x:(-x[0], -x[1], x[2]))
    return ["pid" + str(x[2]) for x in ans]

solution(["2020-02-02 uid141 pid141", "2020-02-03 uid141 pid32", "2020-02-04 uid32 pid32", "2020-02-05 uid32 pid141"], 31, "2020-01-30")