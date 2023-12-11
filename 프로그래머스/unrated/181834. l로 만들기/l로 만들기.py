def solution(myString):
    myString = list(myString)
    
    for i in range(0, len(myString)):
        if( ord(myString[i]) < ord("l") ):
            myString[i] = "l"
            
    return ''.join(myString)