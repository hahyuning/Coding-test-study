n = int(input())

for _ in range(n):
    num_list = list(map(int, input().split()))
    num_list.sort(reverse=True)
    print(num_list[2])