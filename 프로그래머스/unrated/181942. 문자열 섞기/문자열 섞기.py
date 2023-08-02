def solution(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    result = []
    
    for i in range(0, len(str1)):
        result.append(str1[i])
        result.append(str2[i])
    
    return ''.join(result)