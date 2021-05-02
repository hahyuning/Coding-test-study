def partial_sum(index, sum):
    global cnt
    # 종료 조건: 인덱스가 n까지 온 경우
    if index == n:
        if sum == s:
            cnt += 1
        return

    # a[index]를 사용하는 경우
    partial_sum(index + 1, sum + a[index])
    # a[index]를 사용하지 않는 경우
    partial_sum(index + 1, sum)

# --------------------------------------
n, s = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
partial_sum(0, 0)

# 합이 0인 경우는 아무것도 사용하지 않은 경우를 포함하므로 -1
if s == 0:
    cnt -= 1
print(cnt)