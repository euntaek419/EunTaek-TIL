def solution(numbers):
    
    a = 0
    for i in numbers:
        a = a + i
    
    return a / len(numbers)