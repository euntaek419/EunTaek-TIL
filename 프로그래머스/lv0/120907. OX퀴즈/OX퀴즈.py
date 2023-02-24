def solution(quiz):
    
    answer = []
    
    for i in range(0, len(quiz)):
        result = quiz[i].split()
        
        if(result[1] == "+"):
            A = int(result[0]) + int(result[2])
            
            if( int(result[4]) == A ):
                answer.append("O")
            else:
                answer.append("X")
        
        elif(result[1] == "-"):
            A = int(result[0]) - int(result[2])
            
            if( int(result[4]) == A ):
                answer.append("O")
            else:
                answer.append("X")
        
    return answer