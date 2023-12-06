def solution(myString):
    count = 0
    result = []
    
    for i in myString:
        if(i == 'x'):
            result.append(count)
            count = 0
        else:
            count = count + 1
    
    result.append(count)
    
    return result