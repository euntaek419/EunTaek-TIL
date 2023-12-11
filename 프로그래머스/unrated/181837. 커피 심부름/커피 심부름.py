def solution(order): #아메 4500 / 라떼 5000
    result = 0
    for i in order:
        if(i == "cafelatte" or i == "hotcafelatte" or i == "cafelattehot" or
           i == "icecafelatte" or i == "cafelatteice"):
            result = result + 5000
        else:
            result = result + 4500
            print("ame",i)
    return result