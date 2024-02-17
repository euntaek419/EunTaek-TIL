def solution(food):
    result = []
    
    for i in range(1, len(food)):
        if( food[i] % 2 != 0 ):
            food[i] = food[i]-1
    
    print(food) #[1,6,0,2]
    
    for j in range(1, len(food)): #1번부터 끝까지 반복
        for k in range(0, int(food[j]/2)): #번호에 해당하는 수를 반복
            result.append(j)
    
    result2 = result.copy()
    
    result.append(0)
    
    print(result)
    print(result2)
    
    for l in range(len(result2)-1, -1 , -1):
        result.append(result2[l])
    
    
    return str(int(''.join(map(str, result))))