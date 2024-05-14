from collections import Counter

def solution(X, Y):
    X = Counter(X)
    Y = Counter(Y)
    
    # 공통 숫자와 그 빈도를 찾는다
    XY = X & Y
    
    print(XY)
    
    # 공통 숫자들을 기반으로 결과 문자열을 만든다
    result = []
    for n1, n2  in XY.items():
        result.extend([n1] * n2)
    
    # 결과 리스트를 내림차순으로 정렬
    result.sort(reverse=True)
    
    # 결과 문자열이 비어있으면 -1을 반환
    if not result:
        return "-1"
    
    # 결과 문자열을 만든다
    result = ''.join(result)
    
    # 결과가 0으로만 구성된 경우
    if result[0] == '0':
        return '0'
    
    return result