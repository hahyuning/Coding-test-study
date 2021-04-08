n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 0
ans = n + 1
sum = a[0]

while left <= right and right < n:
    # 합이 m보다 작은 경우
    # 오른쪽 포인터를 한 칸 이동하고 sum에 더한다.
    if sum < m:
        right += 1

        if right < n:
            sum += a[right]

    # 합이 m보다 큰 경우
    # sum에서 빼고 왼 쪽 포인터를 한 칸 이동한다.
    elif sum >= m:
        ans = min(ans, right - left + 1)
        sum -= a[left]
        left += 1

        if left > right and left < n:
            right = left
            sum = a[left]

    # 합이 m이 되는 경우
    # 오른쪽 포인터를 한 칸 이동하고 sum에 더한다.
    else:
        ans = min(ans, right - left + 1)
        right += 1

        if right < n:
            sum += a[right]

if ans == n + 1:
    print(0)
else:
    print(ans)