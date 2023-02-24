def solution(cipher, code):
    
    result = []
    cipher = list(cipher)

    for i in range(1, int(len(cipher)/code)+1):
        result.append(cipher[i*code-1])
    
    result = ''.join(map(str, result))
    
    return result