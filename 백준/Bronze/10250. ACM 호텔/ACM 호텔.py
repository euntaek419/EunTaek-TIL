T = int(input())

for i in range(T):
    #층수, 방수, 손님
    H, W, N = map(int, input().split())

    floor = N % H
    if floor == 0:
        floor = H
        room = N // H
    else:
        room = (N // H) + 1

    if room < 10:
        room_num = str(floor) + '0' + str(room)
    else:
        room_num = str(floor) + str(room)

    print(room_num)