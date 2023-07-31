str = input()
str = list(str)
for i in range(0, len(str)):
    if(str[i].isupper() == True):
        str[i] = str[i].lower()
    else:
        str[i] = str[i].upper()
        
str = ''.join(s for s in str)
print(str)
