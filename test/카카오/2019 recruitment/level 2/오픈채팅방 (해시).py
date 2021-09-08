def solution(record):
    ans = []

    record_to_id = dict()
    id_to_nick = dict()
    for i, x in enumerate(record):
        op, user_id = x.split()[0], x.split()[1]
        if op != "Leave":
            nick = x.split()[2]
            id_to_nick[user_id] = nick

        record_to_id[i] = (op, user_id)

    for op, id in record_to_id.values():
        if op == "Enter":
            ans.append(id_to_nick[id] + "님이 들어왔습니다.")
        elif op == "Leave":
            ans.append(id_to_nick[id] + "님이 나갔습니다.")

    return ans
