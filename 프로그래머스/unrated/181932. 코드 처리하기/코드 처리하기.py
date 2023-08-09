def solution(code):
    code = list(code)
    mode = 0
    ret = []
    
    for i in range(0, len(code)):
        if(mode == 0):
            if(code[i] != '1' and i % 2 == 0):
                ret.append(code[i])
            if(code[i] == '1'):
                mode = 1
        else:
            if(code[i] != '1' and i % 2 != 0):
                ret.append(code[i])
            if(code[i] == '1'):
                mode = 0
    
    if(len(ret) > 0):
        return ''.join(ret)
    else:
        return "EMPTY"