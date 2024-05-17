T = int(input())

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for tc in range(1, T + 1):
    result = 1
    array = []
    
    for i in range(9):
        data = list(map(int, input().split()))
        array.append(data)

    #가로줄
    for i in array:
        if(sorted(i) != num ):
            result = 0

    #세로줄
    if(result == 1):
        temp = []
        for i in range(9):
            for j in range(9):
                temp.append(array[j][i])

            if(sorted(temp) != num):
                result = 0
            else:
                temp = []

    #9개 검사
    temp2 = []

    if(result == 1):
        for i in range(0, 3): #00번 검사
            for j in range(0, 3):
                temp2.append(array[i][j])
        if(sorted(temp2) != num):
            result = 0
        else:
            temp2 = []
        
    #-----
    if(result == 1):
        for i in range(3, 6): #01번검사
            for j in range(0, 3):
                temp2.append(array[j][i])
        if(sorted(temp2) != num):
            result = 0
        else:
            temp2 = []

    #-----
    if(result == 1):
        for i in range(6, 9): #02번 검사
            for j in range(0, 3):
                temp2.append(array[j][i])
    
        if(sorted(temp2) != num):
            result = 0
        else:
            temp2 = []

    #----------
    if(result == 1):
        for i in range(0, 3): #10번검사
            for j in range(3, 6):
                temp2.append(array[j][i])
    
        if(sorted(temp2) != num):
            result = 0
        else:
            temp2 = []

    #----------
    if(result == 1):
        for i in range(3, 6): # 11번검사
            for j in range(3, 6):
                temp2.append(array[j][i])
    
        if(sorted(temp2) != num):
            result = 0
        else:
            temp2 = []

    #----------
    if(result == 1):
        for i in range(6, 9): # 12번검사
            for j in range(3, 6):
                temp2.append(array[j][i])
    
        if(sorted(temp2) != num):
            result = 0
        else:
            temp2 = []

    #----------
    if(result == 1):
        for i in range(0, 3): # 20번검사
            for j in range(6, 9):
                temp2.append(array[j][i])
    
        if(sorted(temp2) != num):
            result = 0
        else:
            temp2 = []


    #----------
    if(result == 1):
        for i in range(3, 6): # 21번검사
            for j in range(6, 9):
                temp2.append(array[j][i])

        if(sorted(temp2) != num):
            result = 0
        else:
            temp2 = []


    #----------
    if(result == 1):
        for i in range(6, 9): # 22번검사
            for j in range(6, 9):
                temp2.append(array[j][i])
    
        if(sorted(temp2) != num):
            result = 0
        else:
            temp2 = []

    print("#{} {}".format(tc, result))