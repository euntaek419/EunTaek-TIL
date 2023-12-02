def solution(myString):
    myString = list(myString)
    
    for i in range(0, len(myString)):
        if(myString[i] == 'a' or myString[i] == 'A'):
            myString[i] = myString[i].upper()
        else:
            myString[i] = myString[i].lower()
            
    return ''.join(myString)