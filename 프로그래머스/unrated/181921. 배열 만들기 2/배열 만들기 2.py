def solution(l, r):
    result = []
    for i in range(l, r + 1):
        if all(number in '05' for number in str(i)):
            result.append(i)
    return result if result else [-1]