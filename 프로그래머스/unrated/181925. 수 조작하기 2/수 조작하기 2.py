def solution(numLog):
    a = []
    num = numLog[0]
    
    for i in range(0, len(numLog)):
        if(num + 1 == numLog[i] ):
            a.append('w')
            num = num + 1
            
        if(num - 1 == numLog[i] ):
            a.append('s')
            num = num - 1
            
        if(num + 10 == numLog[i] ):
            a.append('d')
            num = num + 10
            
        if(num - 10 == numLog[i] ):
            a.append('a')
            num = num - 10
    
    return ''.join(a)