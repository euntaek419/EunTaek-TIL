a,b,v = map(int, input().split()) #올라감 미끄러짐 정상

result = (v - b - 1) // (a - b) + 1

print(result)