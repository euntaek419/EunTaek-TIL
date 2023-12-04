def solution(strArr):
    
    result = []
    
    for i in strArr:
        for j in range(0, len(i)-1):
            #print(i[j:j+2])
            if(i[j:j+2] == "ad"):
                result.append(i)
                break
    
    for k in range(0, len(result)):
        strArr.remove(result[k])
    
    return strArr