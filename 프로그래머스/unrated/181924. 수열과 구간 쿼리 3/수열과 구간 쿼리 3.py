def solution(arr, queries):
    a = 0
    for x,y in queries:
        a = arr[x]
        arr[x] = arr[y]
        arr[y] = a

    return arr