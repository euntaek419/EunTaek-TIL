def solution(myStr):
    
    myStr = list(myStr)
    
    for i in range(0, len(myStr)):
        if(myStr[i] == "a"):
            myStr[i] = " "
        elif(myStr[i] == "b"):
            myStr[i] = " "
        elif(myStr[i] == "c"):
            myStr[i] = " "
    
    myStr = ''.join(myStr)
    
    myStr = myStr.split()
    
    if(myStr == []):
        return ["EMPTY"]
    else:
        return myStr
    