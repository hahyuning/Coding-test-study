ipv6 = input()
# 2001:db8:85a3::8a2e:370:7334
# 25:09:1985:aa:091:4846:374:bb
# ::1
parts = ipv6.split(':')
# parts = ["2001", "db8", "85a3", "", "8a2e", "370", "7334"]
# parts = ["25", "09", "1985", "aa", "091", "4846", "374", "bb"]
# parts = ["", "", "1"]
if parts.count('') > 1: # ::1, ::1
    # parts = ["", "", "1"]
    parts.remove('')
    # parts = ["", "1"]
if len(parts) < 8:
    # parts = ["2001", "db8", "85a3", "", "8a2e", "370", "7334"]
    # parts = ["", "1"]
    index = parts.index('')
    # parts = ["2001", "db8", "85a3", "", "8a2e", "370", "7334"]
    #                                 index
    # parts = ["", "1"]
    #          index
    parts[index:index+1] = ['0']*(8-len(parts)+1)
    # parts = ["2001", "db8", "85a3", "0", "0", "8a2e", "370", "7334"]
    #                                 index
    # parts = ["0", "0", "0", "0", "0", "0", "0", 1"]
    #          index
parts = [part.zfill(4) for part in parts]
print(':'.join(parts))