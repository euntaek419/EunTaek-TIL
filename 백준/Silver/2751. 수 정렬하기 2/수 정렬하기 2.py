import sys
input = sys.stdin.readline

T = int(input())

array = []

for i in range(0, T):
    array.append(int(input()))

for i in sorted(array):
    print(i)