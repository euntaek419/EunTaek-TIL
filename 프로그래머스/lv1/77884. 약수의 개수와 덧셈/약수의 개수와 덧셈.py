def solution(left, right):
    
    a = [] #24,25,26,27
    b = []
    c = 0
    
    for i in range(left, right+1):
        a.append(i)
    
    for j in range(0, len(a)): #j = 0,1,2,3,4 수의 갯수만큼 반복
        for k in range(1, a[j]+1): #k = 각 숫자 24 25 26 27 을 0부터 반복
            if(a[j] % k == 0):
                b.append(k)
        
        if(len(b) % 2 == 0):
            c = c + k
            b = [] #값 초기화
        else:
            c = c - k
            b = []
    
    return c