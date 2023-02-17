def solution(letter):
    mos = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z"}
    result = ""
    letter = letter.split(" ")
    for i in letter:
        for m in mos:
            if(i == m):
                result = result + mos[i]
    return result
