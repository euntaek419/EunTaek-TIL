def solution(s, n):
    result = []
    
    for i in s:
        if(i == " "):
            result.append(" ")
        elif( i.isupper() == True):
            if( ord(i)+n >= 91 ):
                result.append(chr(ord(i)+n - 26))
            else:
                result.append(chr(ord(i)+n))
                
        elif( i.isupper() == False):
            if( ord(i)+n >= 123 ):
                result.append(chr(ord(i)+n - 26))
            else:
                result.append(chr(ord(i)+n))
    return ''.join(result)