n = int(input())
num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

max_val = -1e9
min_val = 1e9

def dfs(num, k):
    global max_val, min_val

    if k == n:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return 

    if op_list[0] > 0:
        op_list[0] -= 1
        dfs(num + num_list[k], k + 1)
        op_list[0] += 1
    if op_list[1] > 0:
        op_list[1] -= 1
        dfs(num - num_list[k], k + 1)
        op_list[1] += 1
    if op_list[2] > 0:
        op_list[2] -= 1
        dfs(num * num_list[k], k + 1)
        op_list[2] += 1
    if op_list[3] > 0:
        op_list[3] -= 1
        dfs(int(num / num_list[k]), k + 1)
        op_list[3] += 1

dfs(num_list[0], 1)
print(max_val)
print(min_val)