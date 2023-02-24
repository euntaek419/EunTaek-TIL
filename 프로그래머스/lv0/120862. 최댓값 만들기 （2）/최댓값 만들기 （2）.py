def solution(numbers):
    
    numbers = sorted(numbers)
        
    if(numbers[0] * numbers[1] > numbers[len(numbers)-2] * numbers[len(numbers)-1] ):
        return numbers[0] * numbers[1]
    else :
        return numbers[len(numbers)-2] * numbers[len(numbers)-1]