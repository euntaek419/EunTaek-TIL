def solution(n):
    bn1 = bin(n)[2:] #bin number
    bn1 = list(bn1)
    count = 0
    result = ''
    for i in range(0, len(bn1)): #n의 1 갯수
        if(bn1[i] == '1'):
            count += 1
    
    for i in range(n+1, 1000000):
        count2 = 0
        bn2 = bin(i)[2:]
        bn2 = list(bn2)
        for j in range(0, len(bn2)):
            if(bn2[j] == '1'):
                count2 += 1
        
        if(count == count2):
            result = ''.join(bn2)
            break;
    result = '0b' + result
    
    return int(result, 2)