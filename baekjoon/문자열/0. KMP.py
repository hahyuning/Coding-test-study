def KMP(pat, txt):
    m = len(pat)
    n = len(txt)

    lps = [0] * m

    LPS(pat, lps)

    i = 0  # txt 의 인덱스
    j = 0  # pat 의 인덱스
    while i < n:
        # 문자열이 같은 경우 양쪽 인덱스를 모두 증가시킴
        if pat[j] == txt[i]:
            i += 1
            j += 1
        # 패턴을 찾지 못한 경우
        elif pat[j] != txt[i]:
            # j != 0인 경우는 짧은 lps 에 대해 재검사
            if j != 0:
                j = lps[j-1]
            # j == 0이면 일치하는 부분이 없으므로 인덱스 증가
            else:
                i += 1

        # 패턴을 찾은 경우 시작 인덱스 반환
        if j == m:
            print(i-j)
            # 이전 인덱스의 lps 값을 참조하여 계속 검색
            j = lps[j-1]

def LPS(pat, lps):
    # 접두사와 접미사가 같을 때 가장 긴 길이
    length = 0
    i = 1
    while i < len(pat):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # 일치하지 않는 경우
            if length != 0:
                # 이전 인덱스에서는 같았으므로 length 를 줄여서 다시 검사
                length = lps[length - 1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
                lps[i] = 0
                i += 1

# txt = "ABABDABACDABABCABAB"
# pat = "ABABCABAB"
txt = 'ABXABABXAB'
pat = 'ABXAB'
KMP(pat, txt)