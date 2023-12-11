def solution(str1, str2):
    for i in range(0, len(str2)):
        if(str2[i:i+len(str1)] == str1):
            return 1
    
    return 0