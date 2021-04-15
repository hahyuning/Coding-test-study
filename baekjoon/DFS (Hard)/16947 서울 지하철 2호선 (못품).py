n = int(input())
subway = []
check = [0] * n

def cycle_check(x, prev):
    # -2: 사이클을 찾았으나 사이클에 포함되지 않는 경우
    # -1: 사이클을 찾음
    # 0 ~ n - 1: 사이클을 찾은 경우 사이클의 시작 인덱스
    if check[x] == 1:
        return x
    check[x] = 1
    for y in subway[x]:
        if y == prev:
            continue
        result = cycle_check(y, x)
        if result == -2:
            return -2
        if result > 0:
            check[x] = 2
            if x == result:
                return -2
            else:
                return result
    return -1

