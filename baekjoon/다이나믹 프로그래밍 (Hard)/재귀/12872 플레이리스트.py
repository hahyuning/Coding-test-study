def solution(i, x):
    y = n - x

    if i == p:
        if y == 0:
            return 1
        else:
            return 0

    if d[i][x] != -1:
        return d[i][x]

    ans = 0
    # 새로운 곡을 추가하는 경우
    if y > 0:
        ans += solution(i + 1, x + 1) * y

    # 이미 들은 노래를 또 추가하는 경우
    # x개 중에 그전 m개의 노래를 제외한 x - m 가지의 경우 가능
    if x > m:
        ans += solution(i + 1, x) * (x - m)

    ans %= 1000000007
    d[i][x] = ans
    return ans

n, m, p = map(int, input().split())

# p개의 플레이리스트에 n개의 노래 모두 추가
# 같은 노래를 추가하려면, 두 노래 사이에 적어도 m개의 곡이 있어야 함
# -> 길이가 m + 1인 플레이리스트의 연속된 일부분은 모두 다른곡 (같은 곡이 들어있는 플레이리스트는 길이가 m + 2)

# 노래는 이미 추가한 노래와 아직 추가히지 않은 노래, 두 그룹으로 나눌 수 있음 (초기상태: 0, n, 종료상태: n, 0)
# d[i][x][y]: i번째 곡을 선택할 때, 두 그룹의 크기
d = [[-1] * (n + 1) for _ in range(p + 1)]
print(solution(0, 0))