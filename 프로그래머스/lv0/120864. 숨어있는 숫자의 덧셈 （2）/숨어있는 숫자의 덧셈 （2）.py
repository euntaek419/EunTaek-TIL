import re
def solution(my_string):
    
    result = re.findall(r'\d+', my_string)
    
    sum = 0
    
    for i in range(0, len(result)):
        result[i] = int(result[i])
        
    for j in range(0, len(result)):
        sum = sum + result[j]
    
    return sum