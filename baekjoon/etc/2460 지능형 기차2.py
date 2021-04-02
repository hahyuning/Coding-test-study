result = 0
people_sum = 0

for i in range(1, 11):
    output_num, input_num = map(int, input().split())
    people_sum += (input_num - output_num)
    result = max(result, people_sum)

print(result)
