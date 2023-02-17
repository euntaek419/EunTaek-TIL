#append로 첫번째거 넣고, 두번째거부터 반복
#append로 2번째거부터 반복 후, 마지막에 append 따로 추가하기
def solution(numbers, direction):
    r = "right"
    ra = []
    l = "left"
    la = []
    
    if(direction == r):
        ra.append(numbers[len(numbers)-1])  
        for raf in range(0, len(numbers)-1):
            ra.append(numbers[raf])     
        return ra
            
    elif(direction == l):
        for laf in range(1, len(numbers)):
            la.append(numbers[laf])        
        la.append(numbers[0])
        return la