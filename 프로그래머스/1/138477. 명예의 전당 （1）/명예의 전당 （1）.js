function solution(k, score) {
    result = [];
    temp = [];

    for (i = 0; i < score.length; i++) {
        if (i < k) {
            temp.push(score[i]);
            temp.sort((a, b) => a - b);
            result.push(temp[0]);
        } else if (i >= k && score[i] > temp[0]) {
            temp.shift();
            temp.push(score[i]);
            temp.sort((a, b) => a - b);
            result.push(temp[0]);
        } else if (i >= k && score[i] <= temp[0]) {
            result.push(temp[0]);
        }
    }
    return result;
}