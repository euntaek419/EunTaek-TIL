def solution(cards1, cards2, goal):
    one = 0
    two = 0
    result = []

    for i in range(len(goal)):
        if(one < len(cards1) and goal[i] == cards1[one]):
            result.append(goal[i])
            one = one + 1
        elif(two < len(cards2) and goal[i] == cards2[two]):
            result.append(goal[i])
            two = two + 1
        else:
            return "No"

    if(goal == result):
        return "Yes"
    else:
        return "No"