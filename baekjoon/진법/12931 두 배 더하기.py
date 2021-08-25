n = int(input())
b = list(map(int, input().split()))
a = [bin(x)[2:] for x in b]

# 두 배 연산
ans = max(len(x) - 1 for x in a)
# 1 더하기 연산
ans += sum(x.count("1") for x in a)
print(ans)