def solution(my_strings, parts):
    result = []
    
    for i in range(0,len(parts)):
        strings = list(my_strings[i])
        
        for j in range(parts[i][0],parts[i][1]+1):    
            result.append(strings[j])
    
    return ''.join(result)