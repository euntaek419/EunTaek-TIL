def solution(lottos, win_nums): #구매한거 / 당첨

    result = []
    
    lottos = sorted(lottos)
    win_nums = sorted(win_nums)
    
    count = 0
    zero = 0
    
    for i in range(0, len(lottos)):
        if(lottos[i] == 0):
            zero += 1
        for j in range(0, len(win_nums)):
            if(lottos[i] == win_nums[j]):
                count += 1
    
    #1등 구하기
    if(count + zero == 6):
        result.append(1)
    elif(count + zero == 5):
        result.append(2)
    elif(count + zero == 4):
        result.append(3)
    elif(count + zero == 3):
        result.append(4)
    elif(count + zero == 2):
        result.append(5)
    else:
        result.append(6)
    
    #꼴등 구하기
    if(count == 6):
        result.append(1)
    elif(count == 5):
        result.append(2)
    elif(count == 4):
        result.append(3)
    elif(count == 3):
        result.append(4)
    elif(count == 2):
        result.append(5)
    else:
        result.append(6)
        
    return result
    