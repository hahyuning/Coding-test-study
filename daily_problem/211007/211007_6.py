n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = max(a)

# i, j 로 만든 눈사람과 lt, rt 로 만든 눈사람의 키 차이 중 최소 구하기
for i in range(n - 3):
    for j in range(i + 3, n):
        lt, rt = i + 1, j - 1

        while lt < rt:
            tmp = a[i] + a[j] - a[lt] - a[rt]

            if abs(tmp) < ans:
                ans = abs(tmp)

            if tmp < 0:
                rt -= 1
            else:
                lt += 1
print(ans)