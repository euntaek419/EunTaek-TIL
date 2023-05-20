def solution(x):
    
    a = x
    
    x = list(str(x))
    
    x =  a / sum(list(map(int, x)))
    
    if(x == int(x)):
        return True
    else:
        return False