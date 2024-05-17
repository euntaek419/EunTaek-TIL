T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    array = []
    newarray = [['0' for i in range(3)] for i in range(n)]

    for i in range(n):
        data = list(map(int, input().split()))
        array.append(data)
    
    temp = 0
    for i in range(n):
        word = ''
        for j in range(n-1, -1, -1):
            word = word + str(array[j][i])
        newarray[temp][0] = word
        temp += 1

    temp = 0
    for i in range(n-1, -1, -1):
        word = ''
        for j in range(n-1, -1, -1):
            word = word + str(array[i][j])
        newarray[temp][1] = word
        temp += 1

    temp = 0
    for i in range(n-1, -1, -1): #03 13 23 / 02 12 22 / 01 11 21
        word = ''
        for j in range(n):
            word = word + str(array[j][i])
        newarray[temp][2] = word
        temp += 1
    
    #print(newarray)
    print('#{}'.format(tc))
    for i in range(0, n):
        print(' '.join(map(str, newarray[i])))