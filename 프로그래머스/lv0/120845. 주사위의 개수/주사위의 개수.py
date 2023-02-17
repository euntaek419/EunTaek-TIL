def solution(box, n):
    
    wid = box[0] // n
    dep = box[1] // n
    hei = box[2] // n
    
    return wid*dep*hei