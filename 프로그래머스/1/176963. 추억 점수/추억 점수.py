def solution(name, yearning, photo):
    score = {}
    result = []
    for i in range(0, len(name)):
        score[name[i]] = yearning[i]
    
    for i in range(0, len(photo)):
        tempScore = 0
        for j in range(0, len(photo[i])):
            if(photo[i][j] in score):
                tempScore = tempScore + score[photo[i][j]]
        result.append(tempScore)
    
    return result