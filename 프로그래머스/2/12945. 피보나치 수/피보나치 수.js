function solution(n) {
    F = [0, 1];
    m = 1234567
    
    for (i = 2; i < n+1; i++) {
        F.push(F[i - 2] % m + F[i - 1] % m);
    }
    
    return F[n] % m
}