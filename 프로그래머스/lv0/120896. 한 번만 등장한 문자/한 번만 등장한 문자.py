def solution(result):
    
    a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = 0
    
    result = list(result)
    
    answer = []
    
    for num in range(0, len(result)):
        if(result[num] == "a"):
            a = a+1
            
        elif(result[num] == "b"):
            b = b+1
            
        elif(result[num] == "c"):
            c = c+1
            
        elif(result[num] == "d"):
            d = d+1
            
        elif(result[num] == "e"):
            e = e+1
            
        elif(result[num] == "f"):
            f = f+1
            
        elif(result[num] == "g"):
            g = g+1
            
        elif(result[num] == "h"):
            h = h+1
            
        elif(result[num] == "i"):
            i = i+1
            
        elif(result[num] == "j"):
            j = j+1
            
        elif(result[num] == "k"):
            k = k+1
            
        elif(result[num] == "l"):
            l = l+1
            
        elif(result[num] == "m"):
            m = m+1
                
        elif(result[num] == "n"):
            n = n+1
                
        elif(result[num] == "o"):
            o = o+1
                
        elif(result[num] == "p"):
            p = p+1
                
        elif(result[num] == "q"):
            q = q+1
                
        elif(result[num] == "r"):
            r = r+1
                
        elif(result[num] == "s"):
            s = s+1
                
        elif(result[num] == "t"):
            t = t+1
                
        elif(result[num] == "u"):
            u = u+1
                
        elif(result[num] == "v"):
            v = v+1
                
        elif(result[num] == "w"):
            w = w+1
                
        elif(result[num] == "x"):
            x = x+1
                
        elif(result[num] == "y"):
            y = y+1
                
        elif(result[num] == "z"):
            z = z+1
        
    
    if(a == 1):
        answer.append("a")
    
    if(b == 1):
        answer.append("b")
    
    if(c == 1):
        answer.append("c")
    
    if(d == 1):
        answer.append("d")
    
    if(e == 1):
        answer.append("e")
    
    if(f == 1):
        answer.append("f")
        
    if(g == 1):
        answer.append("g")
        
    if(h == 1):
        answer.append("h")
        
    if(i == 1):
        answer.append("i")
    
    if(j == 1):
        answer.append("j")
    
    if(k == 1):
        answer.append("k")
    
    if(l == 1):
        answer.append("l")
        
    if(m == 1):
        answer.append("m")
        
    if(n == 1):
        answer.append("n")
        
    if(o == 1):
        answer.append("o")
        
    if(p == 1):
        answer.append("p")
        
    if(q == 1):
        answer.append("q")
    
    if(r == 1):
        answer.append("r")
        
    if(s == 1):
        answer.append("s")
        
    if(t == 1):
        answer.append("t")
        
    if(u == 1):
        answer.append("u")
        
    if(v == 1):
        answer.append("v")
        
    if(w == 1):
        answer.append("w")
        
    if(x == 1):
        answer.append("x")
        
    if(y == 1):
        answer.append("y")
        
    if(z == 1):
        answer.append("z")
        
    
    answer = " ".join(answer)
    answer = answer.replace(" ", "")
    print(answer)
    
    return answer