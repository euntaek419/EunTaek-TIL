def solution(n_str):
    n_str = list(n_str)
    for i in range(0, len(n_str)):
        if(n_str[i] == '0'):
            n_str[i] = ''
        else:
            break;
            
    
    return ''.join(n_str)