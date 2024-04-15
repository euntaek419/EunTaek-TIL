function solution(s) {
    s = s.split(' ')
    s = s.map(Number)
    
    result = []
    result.push(String(Math.min(...s)))
    result.push(String(Math.max(...s)))
    
    return result.join(' ')
}