n, s = map(int, input().split())
a = list(map(int, input().split()))

# 절반으로 나눠서 생각
m = n // 2
n = n - m

first = [0] * (1 << n)
second = [0] * (1 << m)

# 만들 수 있는 모든 조합마다 합 구하기
for i in range(1 << n):
    for k in range(n):
        if i & (1 << k) > 0:
            first[i] += a[k]

for i in range(1 << m):
    for k in range(m):
        if i & (1 << k) > 0:
            second[i] += a[k + n]

first.sort()
second.sort(reverse=True)

first_left = second_left = 0
first_right = (1 << n)
second_right = (1 << m)
ans = -1

while first_left < first_right and second_left < second_right:
    if first[first_left] + second[second_left] == s:
        # 합이 같은 경우 세기
        tmp1 = 1
        tmp2 = 1

        first_left += 1
        second_left += 1
        while first_left < n and first[first_left] == first[first_left - 1]:
            tmp1 += 1
            first_left += 1
        while second_left < m and second[second_left] == second[second_left - 1]:
            tmp2 += 1
            second_left += 1

        ans += tmp1 * tmp2

    elif first[first_left] + second[second_left] < s:
        first_left += 1
    else:
        second_left += 1

print(ans)
