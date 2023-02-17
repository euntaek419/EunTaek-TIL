def solution(dot):
    if(dot[0] > 0):
        A = 1 #양수
    else : A = 0 #음수
    
    if(dot[1] > 0):
        B = 1 #양수
    else : B = 0 #음수
    
    if(A == 1 and B == 1):
        return 1
    elif(A == 0 and B == 1):
        return 2
    elif(A == 0 and B == 0):
        return 3
    elif(A == 1 and B == 0):
        return 4         