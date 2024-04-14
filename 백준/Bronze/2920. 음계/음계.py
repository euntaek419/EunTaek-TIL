num = input()

ascending = '12345678'
descending = '87654321'

if(''.join(num.split()) == ascending):
    print('ascending')
elif(''.join(num.split()) == descending):
    print('descending')
else:
    print('mixed')