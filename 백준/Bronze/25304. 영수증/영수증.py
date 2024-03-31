a = int(input())

b = 0

T = int(input())
for i in range(T):
    A, B = map(int, input().split());
    b = b + A*B

if(a == b):
    print("Yes")
else:
    print("No")