def solution(sizes):
    가로 = []
    세로 = []
    temp = 0
    
    for i in range(0, len(sizes)):
        가로.append(sizes[i][0])
        세로.append(sizes[i][1])
    
    
    if(max(가로) > max(세로)):
        for i in range(0, len(sizes)):
            if(세로[i] > 가로[i]):
                temp = 가로[i]
                가로[i] = 세로[i]
                세로[i] = temp
    else:
        for i in range(0, len(sizes)):
            if(가로[i] > 세로[i]):
                temp = 가로[i]
                가로[i] = 세로[i]
                세로[i] = temp
    
    return max(가로) * max(세로)