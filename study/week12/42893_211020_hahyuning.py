from collections import defaultdict
import re

def solution(word, pages):
    n = len(pages)
    # 기본점수: 해당 웹페이지의 텍스트 중 검색어가 등장하는 횟수
    # 외부링크수: 해당 웹페이지에서 다른 외부 페이지로 연결된 링크의 수
    # 링크점수: 해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본점수 / 외부 링크수의 총합
    # 매칭점수: 기본점수 + 링크점수

    meta_parser = re.compile("<meta property=\"og:url\" content=(.+?)/>")
    a_parser = re.compile("<a href=(.+?)>")

    page_info = defaultdict(list)
    url_info = defaultdict(list)
    for page in pages:
        url = meta_parser.findall(page)[0][1:-1]

        # 기본점수 계산: 특수 문자를 다 .으로 치환
        tmp = re.sub("[^a-z]+", ".", page.lower()).split(".")
        word_point = tmp.count(word.lower())
        page_info[url].append(word_point)

        # 외부 링크 처리
        a_tags = a_parser.findall(page)
        for a in a_tags:
            url_info[a[1:-1]].append(url)

        page_info[url].append(len(a_tags))


    # 매칭점수 계산
    match_point = [0] * n
    i = 0
    for page, info in page_info.items():
        # 기본점수
        word_point = info[0]

        # 링크점수 계산
        outer_url = url_info[page]
        if outer_url:
            tmp = 0
            for outer in outer_url:
                tmp += page_info[outer][0] / page_info[outer][1]
            word_point += tmp

        match_point[i] = word_point
        i += 1

    return match_point.index(max(match_point))