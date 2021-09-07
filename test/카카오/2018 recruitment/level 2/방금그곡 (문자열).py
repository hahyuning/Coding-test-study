# 각음을 한글자로 변환
def song_change(song):
    song = song.replace('C#', 'c')
    song = song.replace('D#', 'd')
    song = song.replace('F#', 'f')
    song = song.replace('G#', 'g')
    song = song.replace('A#', 'a')

    return song

def solution(m, musicinfos):
    res = []

    for i, x in enumerate(musicinfos):
        s, e, name, song = x.split(",")
        time = int(e.split(":")[0]) * 60 + int(e.split(":")[1]) - int(s.split(":")[0]) * 60 - int(s.split(":")[1])
        song = song_change(song)
        m = song_change(m)

        # 플레이 시간만큼 음악길이 조절
        song = song * (time // len(song)) + song[:time % len(song)]

        print(song)
        if m in song:
            res.append((time, i, name))

    if len(res) == 0:
        return "(None)"

    res.sort(key=lambda x:(-x[0], x[1]))
    return res[0][2]