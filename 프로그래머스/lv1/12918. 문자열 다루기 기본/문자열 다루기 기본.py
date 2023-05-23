def solution(s):
    
    print(len(s))
    
    if(s.isdigit() == True):
        if(len(list(s)) == 4 or len(list(s)) == 6):
            return True
        else :
            return False
    else:
        return False
    
    
    