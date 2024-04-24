def solution(k, score):
    result = []
    temp = []
    
    for i in range(0, len(score)):
        if(i<k):
            temp.append(score[i])
            temp = sorted(temp)
            result.append(temp[0])
        
        if(i >= k and score[i] > temp[0]):
            temp.pop(0)
            temp.append(score[i])
            temp = sorted(temp)
            result.append(temp[0])
        elif(i >= k and score[i] <= temp[0]):
            result.append(temp[0])
            
    return result