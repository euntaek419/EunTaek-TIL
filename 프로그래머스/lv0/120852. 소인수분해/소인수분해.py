#n을 2로 나눠질때까지 계속 나누고
#3으로 나눠질때까지 나누고
#...n으로 나눠질때까지 나누고
#나눈 수들을 result 집합에 넣기.
def solution(n):
    
    result = []
    a = 2
    
    for j in range (1, n):  
        while n % a == 0: 
            n = n/a
            result.append(a)
        
        if( n % a != 0):
            a = a + 1
    
    result = set(result) #중복되는 수 제거
    result = list(result) #리스트로 복귀
    result.sort() #재정렬
    
    return result #리스트 출력