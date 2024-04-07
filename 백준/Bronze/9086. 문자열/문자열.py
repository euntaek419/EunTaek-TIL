import sys
input = sys.stdin.readline

n = int(input())

for i in range(0, n):
    word = input()
    print(word[0:1]+word[-2])