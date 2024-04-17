def solution(s):
    result = []
    for i in s:
        if i == "(":
            result.append(i)
        else:
            if not result:
                return False
            else:
                result.pop()
    return len(result) == 0    