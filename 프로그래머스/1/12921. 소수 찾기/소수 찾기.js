function solution(n) {
    let count = new Array(n+1).fill(true);
    count[0] = count[1] = false;

    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (count[i]) {
            for (let j = i*i; j <= n; j += i) {
                count[j] = false;
            }
        }
    }

    return count.filter(x => x).length;
}