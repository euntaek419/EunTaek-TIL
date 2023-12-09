def solution(rank, attendance):
    result = []
    resultIndex = []
    
    for i in range(0,len(rank)):
        if(attendance[i] == True):
            result.append(rank[i])
            
    result.sort()
    
    for j in range(0, len(result)):
        for k in range(0, len(rank)):
            if(result[j] == rank[k]):
                resultIndex.append(k)
    
    return 10000*resultIndex[0] + 100*resultIndex[1] + resultIndex[2]