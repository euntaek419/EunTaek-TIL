def solution(num_list, n):
    result = []
    for i in range(len(num_list)//n):  #차원 나누기
        result.append(num_list[ n*i : n*(i+1) ])
    return result


