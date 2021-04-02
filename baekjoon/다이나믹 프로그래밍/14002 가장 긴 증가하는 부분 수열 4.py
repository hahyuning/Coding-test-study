n = int(input())
a = list(map(int, input().split()))
# d[i] : a[i]를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
# d[i] = max(d[j] + 1), 0 <= j <= i - 1, a[j] < a[i]
d = [1] * n
# v[i] : a[i]의 앞에 와야 하는 수의 인덱스
v = [-1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            v[i] = j

ans = []
last_index = d.index(max(d))

while last_index > -1:
    ans.append(a[last_index])
    last_index = v[last_index]
ans.reverse()

print(max(d))
print(" ".join(map(str, ans)))