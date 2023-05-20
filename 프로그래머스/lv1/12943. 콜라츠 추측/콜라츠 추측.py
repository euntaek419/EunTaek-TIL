def solution(num):
    if( num == 1):
        return 0
    
    else:
        for i in range(0, 500):
            if(num % 2 == 0):
                num = num / 2
                if( num == 1 ):
                    return i +1
            else:
                num = num *3 +1
                if( num == 1 ):
                    return i +1
    
    return -1
            
    