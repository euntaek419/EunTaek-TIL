def solution(picture, k):
    temp = []
    result = []
    for i in range(0, len(picture)):
        for j in range(0, len(picture[i])):
            for n in range(0, k):
                temp.append(picture[i][j])
        
        for m in range(0, k):
            result.append(''.join(temp))
        
        temp = []
        
    return result