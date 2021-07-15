import sys
sys.setrecursionlimit(10000)

def solution(k, room_number):
    # {체크인 번호:다음 빈방}
    rooms = dict()

    for x in room_number:
        find_room(x, rooms)
    return list(rooms.keys())

def find_room(i, rooms):
    if i not in rooms:
        rooms[i] = i + 1
        return i

    empty = find_room(rooms[i], rooms)
    rooms[i] = empty + 1

    return empty

print(solution(10, [1,3,4,1,3,1]))