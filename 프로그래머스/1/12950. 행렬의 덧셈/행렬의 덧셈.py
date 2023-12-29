def solution(arr1, arr2):
    result = []
    
    arr_length = len(arr1)
    index_length = len(arr1[0])
    
    for i in range(arr_length):
        temp = []
        for j in range(index_length):
            temp.append(arr1[i][j] + arr2[i][j])
            
        result.append(temp)

    return result