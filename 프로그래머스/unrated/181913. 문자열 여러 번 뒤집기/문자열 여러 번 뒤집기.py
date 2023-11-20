def solution(my_string, queries):
    my_string = list(my_string)
    new_string = []
    a = 0
    
    for i in range(0, len(queries)):
        for j in range(queries[i][0], queries[i][1]+1):
            new_string.append(my_string[j])
        
        new_string.reverse()
        
        for k in range(queries[i][0], queries[i][1]+1):
            my_string[k] = new_string[a]
            a = a +1
            
        a = 0
        
    return ''.join(my_string)