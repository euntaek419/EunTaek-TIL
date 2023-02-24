def solution(order):
    
    order = list(map(int, str(order)))
    result = 0
    
    for i in range(0,len(order)):
        if(order[i] == 3):
            result = result + 1
        elif(order[i] == 6):
            result = result + 1
        elif(order[i] == 9):
            result = result + 1    
    
    return result