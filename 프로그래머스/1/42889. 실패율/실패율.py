def solution(N, stages):
    
    result = []
    user = len(stages) #유저 수
    
    answer = [] # 최종 결과
    
    # 1. 각 스테이지의 실패율을 계산하여 배열에 집어넣자
    
    # - n번 스테이지의 실패율 구하기
    
    for i in range(1, N+1): #1스테이지부터 끝까지
        count = 0
        for j in range(0, len(stages)):
            if(stages[j] > i):
                count += 1
        result.append( (user-count) / user )
        user = user - (user-count)
        
    temp = result # 정렬되지 않은 결과
    
    result = sorted(result, reverse=True) # 정렬된 결과
    
    #실패율이 높은 순서부터 인덱스 확인해서 return
    for i in range(0, N):
        if(i > 0 and result[i-1] == result[i]):
            answer.append(answer[i-1] + 1)
        else:
            answer.append(temp.index(result[i]) + 1)
    
    return answer
                
    
        