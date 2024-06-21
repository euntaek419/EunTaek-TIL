def solution(n, words):
    s_word = set()
    p_word = words[0]
    s_word.add(p_word)
    
    for i in range(1, len(words)):
        c_word = words[i]
        
        if p_word[-1] != c_word[0] or c_word in s_word:
            return [(i % n) + 1, (i // n) + 1]
        
        s_word.add(c_word)
        p_word = c_word
    
    return [0, 0]
