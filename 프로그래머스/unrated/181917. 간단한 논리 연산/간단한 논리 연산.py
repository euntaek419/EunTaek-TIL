def solution(x1, x2, x3, x4):
    if(x1 or x2 == True):
        if(x3 or x4 == True):
            return True
        else:
            return False
    else:
        return False