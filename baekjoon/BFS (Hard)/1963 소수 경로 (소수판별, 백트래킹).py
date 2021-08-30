from collections import deque

# 에라토스테네스의 체 (4자리 수에 대해서)
primes = [True] * 10000
for i in range(2, 10000):
    if primes[i] == True:
        for j in range(2 * i, 10000, i):
            primes[j] = False

# ---------------------------------------------------------------
# 어떤 수의 한 자리를 바꿔주는 함수
def change(num, index, digit):
    # 앞자리를 0으로 바꾸는 경우는 -1 리턴
    if index == 0 and digit == 0:
        return  -1

    num_list = list(str(num))
    num_list[index] = str(digit)
    return int("".join(num_list))

# ----------------------------------------------------------------
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    # 바꾼 횟수 기록 (방문 처리까지 같이)
    dist = [-1] * 10000

    q = deque()
    q.append(n)
    dist[n] = 0
    while q:
        now = q.popleft()
        # 4자리에 대해
        for i in range(4):
            # 각 자리의 수를 0부터 9까지 바꿈
            for j in range(10):
                # now 의 i번째 수를 j로 변경
                next = change(now, i, j)
                # 앞자리를 0으로 바꾸는 경우를 제외하고
                if next != -1:
                    # 소수인지 확인, 방문 여부 확인
                    if primes[next] == True and dist[next] == -1:
                        q.append(next)
                        dist[next] = dist[now] + 1

    print(dist[m])