def solution(num, total):
    
    answer = []
    count = 0
    
    for i in range(1,num):
        count = count + i

    first = int( ( total - count ) / num)

    for i in range(0,num):
        answer.append(first+i)

    return answer