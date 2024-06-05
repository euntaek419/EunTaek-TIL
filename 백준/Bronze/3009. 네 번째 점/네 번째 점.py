n1, n2 = map(int, input().split())
n3, n4 = map(int, input().split())
n5, n6 = map(int, input().split())

n7 = n8 = 0
if(n1 == n3):
    n7 = n5
elif(n1 == n5):
    n7 = n3
elif(n3 == n5):
    n7 = n1

if(n2 == n4):
    n8 = n6
elif(n2 == n6):
    n8 = n4
elif(n4 == n6):
    n8 = n2

print(n7, n8)