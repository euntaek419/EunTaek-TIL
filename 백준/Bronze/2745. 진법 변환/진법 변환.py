def baseN_to_base_10(number, base):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    for i in range(len(number)):
        digit = number[-(i + 1)]
        if digit.isdigit():
            result += int(digit) * (base ** i)
        else:
            result += alphabet.index(digit) * (base ** i)
    return result

n, b = input().split()
result = baseN_to_base_10(n, int(b))
print(result)