function solution(answers) {
    a = []
    b = []
    c = []
    
    for (i = 0; i < 2000; i++) {
        a = a.concat([1, 2, 3, 4, 5]);
    }
    
    for (i = 0; i < 1250; i++) {
        b = b.concat([2, 1, 2, 3, 2, 4, 2, 5]);
    }
    
    for (i = 0; i < 1000; i++) {
        c = c.concat([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]);
    }
    
    score = [0, 0, 0];
    result = [];
    
    for (i = 0; i < answers.length; i++) {
        if (answers[i] === a[i]) {
            score[0] += 1;
        }
        if (answers[i] === b[i]) {
            score[1] += 1;
        }
        if (answers[i] === c[i]) {
            score[2] += 1;
        }
    }
    
    for (i = 0; i < 3; i++) {
        if (score[i] === Math.max(...score)) {
            result.push(i + 1);
        }
    }
    
    return result;
}