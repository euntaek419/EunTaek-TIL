def solution(people, limit):
    answer = 0
    people.sort()  # 무게 순으로 정렬
    light = 0
    heavy = len(people) - 1
    
    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        answer += 1
        
    return answer

            
    
    
    return count
    
    