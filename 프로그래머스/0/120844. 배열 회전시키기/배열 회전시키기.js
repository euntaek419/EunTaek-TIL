function solution(numbers, direction) {
    result = []
    if(direction == "right"){
        result.push(numbers[numbers.length - 1]);
        for(i = 0; i < numbers.length - 1; i++) {
            result.push(numbers[i])
        }
        return result
    }
    
    else{
        for(i=1; i < numbers.length; i++) {
            result.push(numbers[i])
        }
        result.push(numbers[0])
        return result
    }
}