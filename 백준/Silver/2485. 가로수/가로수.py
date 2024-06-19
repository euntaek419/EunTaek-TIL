import sys
input = sys.stdin.readline
from math import gcd


n = int(input())

a = int(input())

array = []

for i in range(n-1):
    num = int(input())
    array.append(num - a)
    a = num

g = array[0]
for j in range(1, len(array)):
    g = gcd(g, array[j])

result = 0
for each in array:
    result += each // g - 1

print(result)