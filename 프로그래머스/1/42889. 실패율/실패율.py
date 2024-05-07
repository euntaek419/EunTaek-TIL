def solution(N, stages):
    result = []
    user = len(stages) # 유저 수
    
    answer = [] # 최종 결과
    
    for i in range(1, N+1):
        count = stages.count(i)  # i 스테이지에 머물러 있는 사람 수
        if user == 0:  # 분모가 0이 되는 것을 방지
            fail = 0
        else:
            fail = count / user  # 실패율 계산
        result.append((i, fail))  # (스테이지 번호, 실패율) 형태로 저장
        user -= count  # 다음 계산을 위해 user 수 업데이트
    
    # 실패율을 기준으로 내림차순 정렬, 실패율이 같다면 스테이지 번호가 작은 순으로 정렬
    result.sort(key=lambda x: (-x[1], x[0]))
    
    # 최종 결과 추출 (스테이지 번호)
    for i in result:
        answer.append(i[0])
    
    return answer
