def solution(n, lost, reserve):
    result = []
    count = 0
    
    lost = sorted(lost)
    reserve = sorted(reserve)
    
    new_lost = []
    new_reserve = []
    
    for i in lost:
        if i not in reserve:
            new_lost.append(i)
    
    for i in reserve:
        if i not in lost:
            new_reserve.append(i)
                
    
    # 모두 가지고 있다고 가정
    for i in range(0, n):
        result.append(1)
        
    # 잃어버린 사람 추려내기
    for i in new_lost:
        result[i-1] -= 1
        
    for i in new_reserve:
        result[i-1] += 1
                
    # 빌려줄 수 있으면 앞쪽 사람부터 빌려주기
    for i in new_reserve:
        if(i > 1 and result[i-2] == 0): # 2번째보다 크면 앞으로 빌려주기 가능
            result[i-2] += 1
            continue # 앞 학생에게 빌려주었으면 건너뛰기

        if(i < n and result[i] == 0): # 또는 뒷 번호에 빌려주기
            result[i] += 1
    
    # 세기
    for i in result:
        if(i >= 1):
            count += 1
    
    return count