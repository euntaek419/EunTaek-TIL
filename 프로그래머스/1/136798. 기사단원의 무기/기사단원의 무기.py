def solution(number, limit, power):
    count = [0] * (number + 1)  # 각 숫자의 약수의 개수를 담을 리스트 초기화
    result = 0

    for i in range(1, number+1):
        for j in range(i, number+1, i):  # i의 배수들에 대해 약수의 개수를 증가
            count[j] += 1
    
    for i in count:
        if i > limit:
            result += power
        else:
            result += i

    return result