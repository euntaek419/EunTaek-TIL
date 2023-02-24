def solution(array, height):
    
    a = 0
    for i in array:
        if(i > height):
            a = a + 1
        
    return a