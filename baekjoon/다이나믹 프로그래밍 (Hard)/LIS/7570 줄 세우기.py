n = int(input())
a = list(map(int, input().split()))

# 가장 긴 증가 수열을 찾되 연속된 수를 가진 증가수열을 찾기
d = [0] * (n + 1)
for i in a:
    # i - 1 이 연속된 증가 수열에 포함되지 않는 경우
    if d[i - 1] == 0:
        d[i] += 1
    # 포함되는 경우
    else:
        d[i] = d[i - 1] + 1

print(n - max(d))