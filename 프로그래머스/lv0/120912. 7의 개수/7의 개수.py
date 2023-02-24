def solution(array):
    
    result = 0
    
    array = int(''.join(map(str, array)))
    array = list(str(array))
    
    for i in range(0, len(array)):
        if( array[i] == '7'):
            result = result + 1
    
    return result


