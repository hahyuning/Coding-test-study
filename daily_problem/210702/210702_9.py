n = int(input())
if n >= 1023:
    print(-1)
elif n == 0:
    print(0)
else:
    cnt = 0
    num = 1
    while True:
        str_num = str(num)
        check = True
        if len(str_num) == 1:
            pass
        else:
            for i in range(1, len(str_num)):
                if int(str_num[i]) < int(str_num[i - 1]):
                    continue
                else:
                    # 다음 감소하는 수로 num 수정
                    start = str_num[:i - 1]
                    mid = str(int(str_num[i - 1]) + 1)
                    end = '0' + str_num[i + 1:]
                    num = int(start + mid + end)
                    check = False
                    break
        if check:
            cnt += 1
            if cnt == n:
                print(num)
                break
            num += 1
