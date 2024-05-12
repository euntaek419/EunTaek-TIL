def solution(n, lost, reserve):
    result = []
    count = 0
    
    lost = sorted(lost)
    reserve = sorted(reserve)
    
    #모두 가지고 있다고 가정
    for i in range(0, n):
        result.append(1)
    
    #여분 있는 사람 찾아내기
    for i in reserve:
        result[i-1] += 1
        
    #잃어버린 사람 추려내기
    for i in lost:
        result[i-1] -= 1
                
    
    #빌려줄 수 있으면 앞쪽 사람부터 빌려주기
    for i in reserve:
        if(i > 2 and result[i-2] == 0 and result[i-1] == 2): #2번째보다 크면 앞으로 빌려주기 가능
            result[i-2] += 1
            result[i-1] -= 1

        elif(i < n and result[i] == 0 and result[i-1] == 2): # 또는 뒷 번호에 빌려주기
            result[i] += 1
            result[i-1] -= 1

    print(result)
    
    #세기
    for i in result:
        if(i >= 1):
            count += 1
    
    return count