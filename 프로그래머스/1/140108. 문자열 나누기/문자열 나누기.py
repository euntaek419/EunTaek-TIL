def solution(s):
    s = list(s)
    word = ''
    temp = ''
    
    result = []
    
    count = 0
    
    for i in range(0, len(s)):
        if(count == 0):
            result.append(temp)
            temp = ''
            word = s[i]
        
        if(s[i] == word):
            temp = temp + s[i]
            count += 1
            
        elif(s[i] != word):
            count -= 1
            temp = temp + s[i]
    
    return len(result)
            
        
        