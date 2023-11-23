def solution(my_string, m, c):
    if(m == 1 and c == 1):
        return my_string
    
    my_string = list(my_string)
    result = []
    
    for i in range(c-1, len(my_string), m):
        result.append(my_string[i])
    
    return ''.join(result)