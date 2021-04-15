n, s = map(int, input().split())
a = list(map(int, input().split()))

m = n // 2
n = n - m

first = [0] * (1 << n)
second = [0] * (1 << m)

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
ans = 0

while first_left < first_right and second_left < second_right:
    if first[first_left] + second[second_left] == s:
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

if s == 0:
    ans -= 1
print(ans)
