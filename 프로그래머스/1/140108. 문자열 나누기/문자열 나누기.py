def solution(s):
    s = list(s)
    word = ''
    
    count = result = 0
    
    for i in range(0, len(s)):
        if(count == 0):
            word = s[i]
            result += 1
        
        if(s[i] == word):
            count += 1
            
        elif(s[i] != word):
            count -= 1

    return result