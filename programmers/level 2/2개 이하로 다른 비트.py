def solution(numbers):
    ans = []

    for num in numbers:
        if num % 2 == 0:
            bin_num = list(bin(num)[2:])
            bin_num[-1] = "1"
        else:
            bin_num = "0" + bin(num)[2:]
            zero = bin_num.rfind("0")

            bin_num = list(bin_num)
            bin_num[zero] = "1"
            bin_num[zero + 1] = "0"

        ans.append(int("".join(bin_num), 2))
    return ans