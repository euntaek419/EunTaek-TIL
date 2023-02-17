def solution(slice, n): #피자조각수 slick / 먹는 사람 n
    
    r = 0 #시켜야 하는 피자 수
    
    if(n % slice == 0):  #슬라이스로 나머지가 0이면 그대로 나누기
        r = n // slice
    
    elif(n % slice >= 1): #슬라이스로 나머지가 1 이상이면 한 판 추가하기
        r = n // slice + 1
        
    return r