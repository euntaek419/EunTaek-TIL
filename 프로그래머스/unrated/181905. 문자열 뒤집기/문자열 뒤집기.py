def solution(my_string, s, e):
    my_string = list(my_string)
    new_string = []
    num = 0
    
    for i in range(s,e+1):
        new_string.append(my_string[i])
        
    new_string.reverse()
    
    for j in range(s, e+1):
        my_string[j] = new_string[num]
        num = num + 1
    
    return ''.join(my_string)