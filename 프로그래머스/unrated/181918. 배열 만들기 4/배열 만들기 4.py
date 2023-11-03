def solution(arr):
    i = 0
    stk = []
    
    while i < len(arr):
        if(stk == []):
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]: #-1번째 인덱스는 마지막 인덱스!!!!!
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            stk.pop()
    
    return stk