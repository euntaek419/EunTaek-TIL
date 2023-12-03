def solution(myString, pat):
    num = 0
    for i in range(0, len(myString)):
        if(myString[i:len(pat)+i] == pat):
            num += 1
    return num