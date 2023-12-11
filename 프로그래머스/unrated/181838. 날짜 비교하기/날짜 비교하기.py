def solution(date1, date2):
    
    date1[0] = date1[0] * 10000
    date2[0] = date2[0] * 10000
    
    date1[1] = date1[1] * 100
    date2[1] = date2[1] * 100
    
    print(sum(date1))
    print(sum(date2))
    
    if( sum(date1) >= sum(date2) ):
        return 0
    else:
        return 1