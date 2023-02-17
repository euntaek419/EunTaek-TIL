def solution(rsp):
    reswin = {"2":"0", "0":"5", "5":"2"}
    result = ""
    for i in rsp:
        for j in reswin:
            if(i == j):
                result = result + reswin[i]
    return result