def solution(n, control):
    control = list(control)
    
    for i in range(0, len(control)):
        if(control[i] == 'w'):
            n = n + 1
        if(control[i] == 's'):
            n = n - 1
        if(control[i] == 'd'):
            n = n + 10
        if(control[i] == 'a'):
            n = n - 10
    
    return n