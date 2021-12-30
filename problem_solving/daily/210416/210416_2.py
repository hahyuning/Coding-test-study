n = int(input())

for _ in range(n):
    num = list(map(int, input().split()))
    num.sort(reverse=True)
    print(num[2])