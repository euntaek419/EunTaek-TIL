def solution(n):
    
    count = [True] * (n+1)
    count[0] = count[1] = False
    
    for i in range(2, int(n**0.5)+1): #2부터 제곱근까지 소수를 구하기
        if count[i]:
            for j in range(i*i, n+1, i):
                count[j] = False
    
    return sum(count)