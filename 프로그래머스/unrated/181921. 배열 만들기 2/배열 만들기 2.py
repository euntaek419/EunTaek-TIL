def solution(l, r):
    result = []
    for i in range(l, r+1):
        if(i % 5 == 0): # 5의 배수이면, 다음 작업
            if('1' not in list(str(i))):
                if('2' not in list(str(i))):
                    if('3' not in list(str(i))):
                        if('4' not in list(str(i))):
                            if('6' not in list(str(i))):
                                if('7' not in list(str(i))):
                                    if('8' not in list(str(i))):
                                        if('9' not in list(str(i))):
                                            result.append(i)
    if(result == [] ):
        return [-1]
    return result