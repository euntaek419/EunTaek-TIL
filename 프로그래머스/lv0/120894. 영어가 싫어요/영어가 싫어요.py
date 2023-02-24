def solution(numbers):
    
    num = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9 }
    
    numbers = numbers.replace('zero', "zero ")
    numbers = numbers.replace('one', "one ")
    numbers = numbers.replace('two', "two ")
    numbers = numbers.replace('three', "three ")
    numbers = numbers.replace('four', "four ")
    numbers = numbers.replace('five', "five ")
    numbers = numbers.replace('six', "six ")
    numbers = numbers.replace('seven', "seven ")
    numbers = numbers.replace('eight', "eight ")
    numbers = numbers.replace('nine', "nine ")
    
    numbers = numbers.split(" ")
    
    result = []
    
    for i in range(len(numbers)-1):
        result.append(num[numbers[i]])
        
    result = int(''.join(map(str, result)))
    
    return result