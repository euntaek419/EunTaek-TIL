def solution(id_pw, db):
    
    db = sum(db, [])
    
    for i in range(0, len(db)):
        if(db[i] == id_pw[0]):
            if(db[i+1] == id_pw[1]):
                return "login"
            else:
                return "wrong pw"
    
    return "fail"
        
        