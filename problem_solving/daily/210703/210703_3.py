import sys
input = sys.stdin.readline

def solution(i, g_cnt):
    global ans, m_cnt
    if sum(m_check) > m_cnt:
        print(m_check)
        # 연주할 수 있는 음악의 개수가 더 많거나 같은 경우
        # 사용한 기타의 개수가 더 적다면 정답 갱신
        ans = g_cnt
        m_cnt = sum(m_check)
    elif sum(m_check) == m_cnt:
        if ans == -1 or g_cnt < ans:
            ans = g_cnt

    if i >= n:
        return

    # i번째 기타 사용 x
    solution(i + 1, g_cnt)

    # i번째 기타 사용 o
    x = guitar[i]
    idx = []
    for j in range(m):
        if x[j] == "Y":
            if not m_check[j]:
                idx.append(j)
            m_check[j] = True
    solution(i + 1, g_cnt + 1)
    for j in idx:
        m_check[j] = False

n, m = map(int, input().split())
guitar = dict()
for i in range(n):
    a, b = input().rstrip().split()
    guitar[i] = b

m_check = [False] * m
ans = -1
m_cnt = 0
solution(0, 0)
if m_cnt == 0:
    print(-1)
else:
    print(ans)