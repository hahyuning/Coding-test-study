from collections import deque

# 에라토스테네스의 체
primes = [False] * 10000
for i in range(2, 10000):
    if primes[i] == False:
        for j in range(2 * i, 10000, i):
            primes[j] = True

# 어떤 수의 한 자리를 바꿔주는 함수
def change(num, index, digit):
    # 앞자리를 0으로 바꾸는 경우는 -1 리턴
    if index == 0 and digit == 0:
        return  -1

    num_list = list(str(num))
    num_list[index] = str(digit)
    return int("".join(num_list))


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    # 방문 여부 체크
    check = [False] * 10000
    # 바꾼 횟수 기록
    dist = [0] * 10000

    q = deque()
    q.append(n)
    check[n] = True
    while q:
        now = q.popleft()
        for i in range(4):
            for j in range(10):
                next = change(now, i, j)
                if next != -1:
                    if primes[next] == False and check[next] == False:
                        q.append(next)
                        dist[next] = dist[now] + 1
                        check[next] = True

    print(dist[m])