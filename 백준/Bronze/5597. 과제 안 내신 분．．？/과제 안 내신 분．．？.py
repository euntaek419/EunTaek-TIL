import sys
input = sys.stdin.readline

work = [False] * 31

for i in range(0, 28):
    a = int(input())
    work[a] = True

work.pop(0)

for i in range(0, len(work)):
    if(work[i] == False):
        print(i+1)