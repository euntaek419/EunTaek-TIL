import sys
input = sys.stdin.readline

n = int(input())

array = set()

for i in range(n):
    a,b = list(input().split())
    if(b == 'enter'):
        array.add(a)
    else:
        array.remove(a)

print('\n'.join(sorted(array, reverse=True)))