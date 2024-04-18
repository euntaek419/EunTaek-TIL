function solution(my_str, n) {
    const result = [];
    let temp1 = [];
    
    for (let i = 0; i < my_str.length; i++) {
        temp1.push(my_str[i]);
        
        if (temp1.length % n === 0 || i + 1 === my_str.length) {
            result.push(temp1.join(''));
            temp1 = [];
        }
    }
    
    return result;
}
