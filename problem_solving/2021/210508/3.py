import bisect

def solution(n, k, cmd):
    answer = ''
    dic = dict()
    for i in range(n):
        dic[i] = 0

    deleted = []

    for c in cmd:
        print(dic, k)
        print(deleted)
        # 위로 이동
        if c[0] == "U":
            a, b = c.split(" ")
            b = int(b)

            target = bisect.bisect_left(deleted, k - b)
            if k < 0 or deleted[target] != k:
                k -= b

            else:
                while True:
                    target = bisect.bisect_left(deleted, k)
                    if k < 0 or deleted[target] != k:
                        break
                    k -= 1

        # 아래로 이동
        if c[0] == "D":
            a, b = c.split(" ")
            b = int(b)

            target = bisect.bisect_left(deleted, k + b)
            if k >= len(deleted) or deleted[target] != k:
                k += b

            else:
                while True:
                    target = bisect.bisect_left(deleted, k)
                    if k >= len(deleted) or deleted[target] != k:
                        break
                    k += 1
        # 삭제: 현재 선택된 행
        # 삭제 후 바로 아래행 선택, 마지막 행인 경우 윗행 선택
        if c[0] == "C":
            deleted.append(k)
            dic[k] -= 1

            for i in range(k + 1, n):
                if dic[i] >= 0:
                    k = i
                    break
            else:
                for i in range(k - 1, -1, -1):
                    if dic[i] >= 0:
                        k = i
                        break

        # 복구
        if c[0] == "Z":
            dic[deleted.pop()] += 1

    for x in dic.keys():
        if dic[x] >= 0:
            answer += "O"
        else:
            answer += "X"
    return answer

print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))