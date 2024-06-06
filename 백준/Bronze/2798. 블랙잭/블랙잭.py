from itertools import *

n, m = map(int, input().split())
data = list(map(int, input().split()))

result = 0

for i in combinations(data, 3):
    if(sum(i) > result and m >= sum(i)):
        result = sum(i)

print(result)