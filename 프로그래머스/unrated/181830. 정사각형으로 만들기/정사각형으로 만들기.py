def solution(arr):
    a = len(arr)
    b = len(arr[0])
    
    if(a == b):
        return arr
    elif(a < b):
        for i in range(a, b):
            arr.append([0] * b)
        return arr
    else:
        for j in range(0, a):
            for k in range(0, a-b):
                arr[j].append(0)
        return arr