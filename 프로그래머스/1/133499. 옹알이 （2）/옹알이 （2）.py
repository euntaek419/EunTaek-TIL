def solution(babbling):
    
    count = 0
    
    for i in range(0, len(babbling)):
        babbling[i] = babbling[i].replace("aya", '*')
        babbling[i] = babbling[i].replace("**", 'aya')
        
        babbling[i] = babbling[i].replace("ye", '&')
        babbling[i] = babbling[i].replace("&&", 'ye')
        
        babbling[i] = babbling[i].replace("woo", '^')
        babbling[i] = babbling[i].replace("^^", 'woo')
        
        babbling[i] = babbling[i].replace("ma", '%')
        babbling[i] = babbling[i].replace("%%", 'ma')
    
    for j in range(0, len(babbling)):
        babbling[j] = babbling[j].replace("*", '')
        babbling[j] = babbling[j].replace("&", '')
        babbling[j] = babbling[j].replace("^", '')
        babbling[j] = babbling[j].replace("%", '')
        
        if(babbling[j] == ''):
            count += 1
        
        print(babbling[i])
    
    return count