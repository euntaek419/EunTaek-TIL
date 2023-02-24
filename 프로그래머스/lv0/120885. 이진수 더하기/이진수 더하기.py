def solution(bin1, bin2):
    
    bin1 = list(bin1)
    bin1.insert(0, '0')
    bin1.insert(1, 'b')
    
    bin2 = list(bin2)
    bin2.insert(0, '0')
    bin2.insert(1, 'b')
    

    bin1 = "".join(bin1)
    bin2 = "".join(bin2)
    
    bin1 = int(bin1, 2)
    bin2 = int(bin2, 2)
    
    result = bin1 + bin2
    
    result = bin(result)
    
    result = result[2:]
    
    return result