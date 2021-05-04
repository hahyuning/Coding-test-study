n, k, m = map(int, input().split())
m -= 1

cnt = 0
start = 0

while True:
    cnt += 1
    removed = (start + k - 1) % n
    if removed == m:
        print(cnt)
        break

    # 동호의 번호보다 앞에서 제거된 경우 번호를 앞으로 1칸 당기기
    if removed < m:
        m -= 1

    n -= 1
    start = removed
