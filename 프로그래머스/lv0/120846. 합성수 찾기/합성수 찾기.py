#1. 4~n까지 반복해서
#2. 합성수인지 찾고
#3. 합성수를 저장하기

def solution(n):
    num = []
    result = []
    for i in range(4, n+1):
        for j in range(1, n+1): 
	        if (i % j == 0):
	            num.append(j)
                
        if(len(num) >= 3):
            result.append(i)
        num = []    
    
    return len(result)
    