n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

def next_permutation(numbers):
    i = n - 1
    while i > 0 and numbers[i - 1] >= numbers[i]:
        i -= 1
    if i <= 0:
        return False

    j = n - 1
    while numbers[j] <= numbers[i - 1]:
        j -= 1

    numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]

    j = n - 1
    while i < j:
        numbers[i], numbers[j] = numbers[j], numbers[i]
        i += 1
        j -= 1

    return True

cities = list(range(n))
ans = 10000000
while True:
    check = True # 모든 도시 순회가 가능한지 확인하는 변수
    tmp = 0
    for i in range(1, n):
        if w[cities[i - 1]][cities[i]] != 0:
            tmp += w[cities[i - 1]][cities[i]]
        else:
            check = False
            break

    # 처음 도시로 돌아올 수 있는지 확인
    if check and w[cities[-1]][cities[0]] != 0:
        tmp += w[cities[-1]][cities[0]]
        ans = min(ans, tmp)

    if not next_permutation(cities):
        break
    # 첫 도시가 0이 아닌 경우 종료
    if cities[0] != 0:
        break
print(ans)