N = int(input())

b = N-1

newN = 2*N-1

for i in range(1, newN+1, +2):
    print(" "*b + "*"*(i))
    b = b-1


b = 1

for i in range(newN-2, 0, -2):
    print(" "*b + "*"*(i))
    b = b+1