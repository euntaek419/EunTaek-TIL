def solution(myString):
    
    myString = list(myString)
    
    for i in range(0, len(myString)):
        if(myString[i] == "x"):
            myString[i] = " "
    
    myString = ''.join(myString)
    
    myString = myString.split()
    
    return sorted(myString)