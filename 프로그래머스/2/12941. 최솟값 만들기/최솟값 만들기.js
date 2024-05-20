function solution(A, B) {
    A.sort((a, b) => b - a);
    B.sort((a, b) => a - b);
    
    result = 0;
    for (i = 0; i < A.length; i++) {
        result += A[i] * B[i];
    }

    return result;
}