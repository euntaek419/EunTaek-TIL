import sys
input = sys.stdin.readline

T = int(input())

array = []

for i in range(0, T):
    n = int(input())
    array.append(n)    

array = sorted(array)

for i in array:
    print(i)