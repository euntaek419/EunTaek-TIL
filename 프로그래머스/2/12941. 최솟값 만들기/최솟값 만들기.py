def solution(A,B):
    A = sorted(A, reverse=True)
    B = sorted(B)
    
    result = 0
    for i in range(0,len(A)):
        result = result + A[i] * B[i]

    return result