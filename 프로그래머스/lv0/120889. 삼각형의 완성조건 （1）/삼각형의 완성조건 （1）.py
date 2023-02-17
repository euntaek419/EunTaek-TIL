def solution(sides):
    
    sides.sort()
    sides.reverse()
    
    answer = sides[0] - sides[1] - sides[2]
    
    if(answer >= 0):
        return 2
    else :
        return 1
    
    