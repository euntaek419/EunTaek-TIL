def solution(my_string, alp):
    my_string = list(my_string)
    
    for i in range(0, len(my_string)):
        if(my_string[i] == alp):
            my_string[i] = alp.upper()
            print(my_string[i])
            
    return ''.join(my_string)