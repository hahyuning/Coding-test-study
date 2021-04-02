n = int(input())
standard_list = list(map(int, input().split()))
standard_list.sort()

if len(standard_list) == 1:
    print(standard_list[0] ** 2)
else:
    print(standard_list[0] * standard_list[-1])