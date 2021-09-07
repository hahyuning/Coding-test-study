def solution(msg):
    dic = dict()

    # 사전 초기화
    i = 1
    for x in range(ord("A"), ord("Z") + 1):
        dic[chr(x)] = i
        i += 1

    if len(msg) == 1:
        return [dic[msg]]

    idx = 1
    ans = []
    now = msg[0]
    cnt = 26

    while idx < len(msg):
        if now + msg[idx] not in dic.keys():
            # 현재 입력과 일치하는 가장 긴 문자열 append
            ans.append(dic[now])

            cnt += 1
            dic[now + msg[idx]] = cnt
            now = msg[idx]
        else:
            now += msg[idx]
        idx += 1

    # 마지막 단어 추가
    ans.append(dic[now])
    return ans