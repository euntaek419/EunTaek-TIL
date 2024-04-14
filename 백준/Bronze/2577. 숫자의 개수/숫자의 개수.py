a = int(input())
b = int(input())
c = int(input())

numbers = {
    '0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0
    }
num = list(str(a*b*c))

num.sort()

for i in range(0, len(num)):
    numbers[str(num[i])] += 1

for i in range(0, 10):
    print(numbers[str(i)])