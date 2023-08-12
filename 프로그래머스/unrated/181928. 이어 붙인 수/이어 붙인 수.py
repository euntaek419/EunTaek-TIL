def solution(num_list):
    a = []
    b = []
    c = ''
    d = ''
    for i in range(0, len(num_list)):
        if(num_list[i] % 2 != 0):
            a.append(str(num_list[i]))
    
    for j in range(0, len(num_list)):
        if(num_list[j] % 2 == 0):
            b.append(str(num_list[j]))
    
    for ii in range(0, len(a)):
        c = c + a[ii]
    
    for jj in range(0, len(b)):
        d = d + b[jj]
        
    
    return int(c) + int(d)