from collections import defaultdict

def solution(genres, plays):
    genres_dic = defaultdict(int)
    for genre, play in zip(genres, plays):
        genres_dic[genre] += play
    # value 값으로 정렬 (내림차순) -> 결과 list
    sorted_genres = sorted(genres_dic.items(), key=lambda x:x[1], reverse=True)

    answer = []
    for gen, p in sorted_genres:
        tmp = []
        # 속한 노래가 많이 재생된 장르를 먼저 수록
        for i in range(len(genres)):
            if gen == genres[i]:
                tmp.append((plays[i], i))
        if len(tmp) == 1:
            answer.append(tmp[0][1])
            continue
        # 장르 내에서 많이 재생된 노래를 먼저 수록
        # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록
        tmp.sort(key=lambda x:(x[0], -x[1]), reverse=True)
        answer.append(tmp[0][1])
        answer.append(tmp[1][1])
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])