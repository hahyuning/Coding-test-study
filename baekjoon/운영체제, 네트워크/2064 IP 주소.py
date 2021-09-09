# 이진수로 변환한 후 앞에서부터 공통되는 가장 긴 문자열 찾기

# 이진수로 변환
def change_to_bin(x):
    a = x.split(".")
    # bin(int(x))[2:] = '1010101'
    # bin(int(x))[2:].zfill(8) = '01010101'
    a = [bin(int(x))[2:].zfill(8) for x in a]
    return "".join(a)

# ip로 변환
def change_to_ip(x):
    ip = ["".join(x[8 * i: 8 * i + 8]) for i in range(4)]
    ip = [int(x, 2) for x in ip]
    return ".".join(map(str, ip))

# 공통되는 가장 긴 문자열의 길이 찾기
def common_prefix(all):
    res = -1
    for i in range(32):
        if len(set(ip[i] for ip in all)) == 1:
            res = i
        else:
            break
    return res

n = int(input())
all = [input() for _ in range(n)]
all = [change_to_bin(x) for x in all]

res = common_prefix(all)
ip = all[0]

net_address = [ip[i] if i <= res else "0" for i in range(32)]
net_mask = ["1" if i <= res else "0" for i in range(32)]
net_address = change_to_ip(net_address)
net_mask = change_to_ip(net_mask)

print(net_address)
print(net_mask)