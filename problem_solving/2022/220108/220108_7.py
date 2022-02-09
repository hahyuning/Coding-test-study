n, k = map(int, input().split())
n += 1
n_list = list(str(n))

idx = 0
max_idx = len(n_list)

while True:
    if n_list.count("5") == k:
        break

    while n_list[max_idx - idx - 1] == "5" and idx + 1 < max_idx:
        idx += 1

    n = int("".join(n_list)) + 10 ** idx
    n_list = list(str(n))
    max_idx = len(n_list)

print("".join(n_list))