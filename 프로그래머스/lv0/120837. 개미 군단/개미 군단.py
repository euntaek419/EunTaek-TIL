def solution(hp):
    ant5 = ant3 = ant1 = 0
    
    ant5c = hp // 5 
    ant5 = hp % 5 
    
    ant3c = ant5 // 3 
    ant3 = ant5 % 3  
    
    ant1 = ant3 / 1
    
    return ant5c + ant3c + ant1