def count(mid):
    global h_cur, h_atk
    res = True
    for i in range(n):
        t, a, h = rooms[i]
        if t == 2:
            h_cur = min(mid, h_cur + h)
            h_atk += a
        else:
            turn_cnt = h // h_atk
            if h % h_atk != 0:
                turn_cnt += 1
            h_cur -= a * (turn_cnt - 1)

            if h_cur <= 0:
                res = False
                break
    return res

n, atk = map(int, input().split())
rooms = []
for _ in range(n):
    # t = 1: 몬스터, a: 공격력, h: 생명력
    # t = 2: 회복, a: 공격력, h: 생명력
    t, a, h = map(int, input().split())
    rooms.append((t, a, h))

lt = 1
rt = 9223372036854775807
ans = rt
while lt <= rt:
    mid = (lt + rt) // 2
    h_cur = mid
    h_atk = atk
    res = count(mid)
    if res:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(ans)