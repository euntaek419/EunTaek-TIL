def solution(strArr):
    num = [0]*31
    
    for i in range(0, len(strArr)):
        
        num[len(strArr[i])] = num[len(strArr[i])] + 1
    
    return max(num)