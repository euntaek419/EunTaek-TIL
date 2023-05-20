def solution(phone_number):
    
    a = len(phone_number)
    
    phone_number = list(phone_number)
    
    for i in range(0, a-4):
        phone_number[i] = '*'
    
    phone_number = ''.join(phone_number)
    
    return phone_number