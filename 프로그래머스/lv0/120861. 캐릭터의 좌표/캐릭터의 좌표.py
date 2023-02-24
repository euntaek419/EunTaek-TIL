def solution(keyinput, board):
    
    x=y=0
    
    x_max = board[0] // 2
    x_min = x_max * -1
    y_max = board[1] // 2
    y_min = y_max * -1
    
    
    result = []
    
    for i in range(0, len(keyinput)):
        if(keyinput[i] == "left" and x_min < x):
            x = x-1
        
        elif(keyinput[i] == "right" and x_max > x):
            x = x+1
        
        elif(keyinput[i] == "up" and y_max > y):
            y = y+1
        
        elif(keyinput[i] == "down" and y_min < y):
            y = y-1
    
    result.append(x)
    result.append(y)
    
    return result