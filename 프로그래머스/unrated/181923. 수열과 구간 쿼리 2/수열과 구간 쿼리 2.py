def solution(arr, queries):
    result = []
    
    for query in queries:
        s, e, k = query
        sub_array = arr[s:e+1]  # 범위 내의 부분 배열 생성
        filtered_array = [x for x in sub_array if x > k]  # 조건을 만족하는 값들로 필터링
        
        if filtered_array:
            result.append(min(filtered_array))  # 필터링된 값 중 최솟값 추가
        else:
            result.append(-1)  # 조건을 만족하는 값이 없을 경우 -1 추가
    
    return result