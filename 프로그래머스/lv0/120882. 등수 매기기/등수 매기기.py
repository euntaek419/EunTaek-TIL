def solution(score):
    
    temp = []
    sort_temp = []
    result = []

    
    for i in range(0, len(score)):
        for j in range(0, 1):
            temp.append(score[i][j] + score[i][j+1])
    
    sort_temp = temp
    
    sort_temp = sorted(sort_temp, reverse = True)
    
    for k in temp:
        result.append(sort_temp.index(k)+1)
    
    return result