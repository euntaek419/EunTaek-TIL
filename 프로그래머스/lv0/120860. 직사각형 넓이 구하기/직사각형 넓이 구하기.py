def solution(dots):
    dots = sum(dots, [])
    
    x = []
    y = []
    
    x.append(dots[0])
    x.append(dots[2])
    x.append(dots[4])
    x.append(dots[6])
    
    y.append(dots[1])
    y.append(dots[3])
    y.append(dots[5])
    y.append(dots[7])
    
    result = ( max(x) - min(x) ) * ( (max(y) - min(y) ) )
    
    return result 