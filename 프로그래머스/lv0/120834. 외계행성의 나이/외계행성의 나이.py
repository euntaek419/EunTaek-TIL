def solution(age):
    answer = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h', '8':'i', '9':'j'}
    
    age = str(age)
    age = list(age)
    
    result = []
    
    for i in age:
        result.append(answer[i])
    
    return ''.join(result) 